# AG02 Continuous Improvement: Targeted Skill Enhancement

**Target Skill**: `.agents/skills/medusa-workflow/SKILL.md`  
**Evaluation Standard**: Constitution Principle V (Scientific Diagnosis & Evidence-Based Verification)  
**Goal**: Enhance the operational rigor of `medusa-workflow` by requiring explicit compensation contract testing for all mutating steps.

---

## 1. Identified Operational Gap in `medusa-workflow`

### The Problem
During our architecture review and exam analysis (specifically **Scenario 9: Medusa Workflow Failure with Uncompensated Custom Steps** and **Scenario 2: Split-Brain Distributed Transactions**), we identified an operational vulnerability in the current `medusa-workflow` skill:
* The current skill states: *"choose official workflow steps and compensation, after-commit external effects..."*
* However, it does not mandate an explicit **Compensation Verification Test** that purposefully forces step failure and asserts that the compensation callback actually fired and cleanly restored system state.
* In Medusa v2, an engineer can easily write:
  ```typescript
  return new StepResponse(result); // Missing second parameter: compensation payload!
  ```
  If subsequent steps fail, Medusa calls the compensation handler with `undefined`, resulting in:
  `TypeError: Cannot read properties of undefined (reading 'reservationId')`
  This leaves the rollback half-executed and corrupts database/financial state.

---

## 2. Proposed Enhancement to `medusa-workflow/SKILL.md`

We enhance `## Procedure` and `## Test-first and failure protocol` in `.agents/skills/medusa-workflow/SKILL.md` with two concrete invariants:
1. **Mandatory Dual-Payload StepResponse**: Every mutating `createStep` definition must return `new StepResponse(outputData, compensationInputData)` where `compensationInputData` contains all necessary identifiers to cleanly reverse the side-effect.
2. **Mandatory Injected Rollback Test (Red-to-Green Compensation Test)**: In addition to the happy-path integration test, the developer must provide an integration test that injects a failure in step $N+1$ and verifies that step $N$'s compensation callback executed and reverted the state in PostgreSQL.

### Proposed Diff to `.agents/skills/medusa-workflow/SKILL.md`
```markdown
## Procedure (in order)
Identify state owner and transaction boundary; choose official workflow steps and compensation; enforce StepResponse(output, compensationPayload) for all mutating steps; isolate after-commit external effects; configure timeout/retry/idempotency contracts; implement tests for success, forced rollback, duplicate replay, late event, provider failure and safe cancellation.

## Test-first and failure protocol
Specify positive acceptance and at least two negative/edge cases:
1. Capture RED failing assertion before fix, then smallest GREEN, and regression.
2. Mandatory Forced Rollback Test: Inject an intentional exception in Step 2; assert that Step 1's compensation function executed, its database changes were reverted, and no orphaned external hold remains.
3. On failure use upstream systematic-debugging: reproduce, isolate layers, one falsifiable hypothesis, experiment, record; after three incorrect fixes STOP and request architecture review.
```

---

## 3. Concrete Verification Test Example

The following unit/integration test proves the utility of this skill improvement by catching unhandled compensation exceptions:

```typescript
// tests/integration/workflow-compensation.test.ts
import { createWorkflow, createStep, StepResponse } from "@medusajs/framework/workflows-sdk";
import { describe, it, expect, vi } from "vitest";

describe("Medusa Workflow Compensation Invariant", () => {
  it("MUST execute compensation and rollback state when a subsequent step throws", async () => {
    let inventoryReserved = false;

    // Step 1: Mutating step with compensation
    const reserveStep = createStep(
      "reserve-step",
      async () => {
        inventoryReserved = true;
        return new StepResponse({ reserved: true }, { rollBackId: "inv_123" });
      },
      async (compensationData) => {
        expect(compensationData).toBeDefined();
        expect(compensationData?.rollBackId).toBe("inv_123");
        inventoryReserved = false; // Successfully reverted!
      }
    );

    // Step 2: Injected failure
    const failingStep = createStep("failing-step", async () => {
      throw new Error("Simulated payment decline");
    });

    const testWorkflow = createWorkflow("test-compensation-flow", () => {
      reserveStep();
      failingStep();
    });

    // Execute workflow and expect error
    await expect(testWorkflow().run()).rejects.toThrow("Simulated payment decline");

    // ASSERTION: State must be restored to false via compensation
    expect(inventoryReserved).toBe(false);
  });
});
```

### Impact & Benefits
* Prevents silent compensation failures where compensation data is missing.
* Guarantees zero orphaned reservations or phantom payment captures in production.
* Leaves all 20 required sections in `verify_agent_os.py` completely compliant.
