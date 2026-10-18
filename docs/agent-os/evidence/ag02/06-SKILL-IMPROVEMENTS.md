# AG02 Continuous Improvement: Targeted Skill Enhancement (Remediated)

**Target Skill**: `.agents/skills/medusa-workflow/SKILL.md`  
**Evaluation Standard**: Constitution Principle V (Scientific Diagnosis & Evidence-Based Verification)  
**Status**: `PROPOSED DESIGN / UNVERIFIED FIXTURE` (No live Medusa runtime executed in AG02)  
**Goal**: Enhance the operational rigor of `medusa-workflow` by defining explicit Compensation Contracts for mutating steps.

---

## 1. Identified Operational Gap in `medusa-workflow`

### The Problem
During our architectural analysis, we identified an operational risk in how workflow steps are authored:
* The current skill states: *"choose official workflow steps and compensation, after-commit external effects..."*
* However, it does not provide guidelines on **when** compensation is required vs when it is superfluous, nor does it mandate defining an explicit **Compensation Contract**.
* In Medusa v2:
  * Read-only query steps (e.g. fetching user data or calculating tax rates) do not mutate state and do **NOT** require a compensation function.
  * Mutating steps (e.g. reserving inventory, deducting points, calling external payment gateways) **MUST** define a structured compensation payload returned as the second argument to `new StepResponse(outputData, compensationPayload)`.
  * If an engineer blindly adds empty compensation callbacks or fails to provide the required compensation payload, the rollback will fail when subsequent steps throw an error.

---

## 2. Proposed Enhancement to `medusa-workflow/SKILL.md`

We refine `## Procedure` and `## Test-first and failure protocol` in `.agents/skills/medusa-workflow/SKILL.md`:

### Proposed Text
```markdown
## Procedure (in order)
1. Identify state owner and transaction boundary.
2. For each step, determine mutability:
   - Read-only steps: return new StepResponse(outputData). Zero compensation overhead.
   - Mutating steps: design an explicit Compensation Contract. Return new StepResponse(outputData, compensationPayload) containing all primary keys and state required to reverse the side effect.
3. Define idempotent compensation handlers that handle partial or repeated execution safely.
4. Isolate non-reversible external effects to post-commit event subscribers where possible.

## Test-first and failure protocol
Specify positive acceptance and at least two negative/edge cases:
1. Capture RED failing assertion before fix, then smallest GREEN, and regression.
2. Mandatory Forced Rollback Design: Write a test fixture where Step 2 intentionally throws an error; verify that Step 1's compensation callback receives the exact compensationPayload and successfully reverts the mutation.
3. On failure use upstream systematic-debugging: reproduce, isolate layers, one falsifiable hypothesis, experiment, record; after three incorrect fixes STOP and request architecture review.
```

---

## 3. Conceptual Verification Test Fixture (Unverified Design)

> [!NOTE]
> The following test fixture is an architectural design specification. Per AG02 invariants, no live Medusa runtime has been started. Actual test execution is scheduled for practical drill stages (AG04–AG07).

```typescript
// Proposed Test Fixture: tests/design/workflow-compensation-contract.test.ts
import { createWorkflow, createStep, StepResponse } from "@medusajs/framework/workflows-sdk";
import { describe, it, expect } from "vitest";

describe("Medusa Workflow Compensation Contract Specification", () => {
  it("MUST execute compensation callback with explicit compensationPayload when subsequent step fails", async () => {
    let mockResourceHeld = false;
    let rollbackExecuted = false;

    // Step 1: Mutating step with explicit compensation contract
    const mutateResourceStep = createStep(
      "mutate-resource-step",
      async () => {
        mockResourceHeld = true;
        // Return output AND explicit rollback payload
        return new StepResponse({ success: true }, { resourceId: "res_abc_123" });
      },
      async (compensationData) => {
        // Contract validation: compensationData must contain resourceId
        if (compensationData?.resourceId === "res_abc_123") {
          mockResourceHeld = false;
          rollbackExecuted = true;
        }
      }
    );

    // Step 2: Injected failure to force workflow compensation
    const failingStep = createStep("failing-step", async () => {
      throw new Error("Simulated downstream payment gateway timeout");
    });

    const testWorkflow = createWorkflow("test-compensation-workflow", () => {
      mutateResourceStep();
      failingStep();
    });

    // Workflow execution must reject
    await expect(testWorkflow().run()).rejects.toThrow("Simulated downstream payment gateway timeout");

    // Post-condition: Resource state must be cleanly reverted
    expect(mockResourceHeld).toBe(false);
    expect(rollbackExecuted).toBe(true);
  });
});
```

### Impact & Benefits
* Differentiates read-only steps from mutating steps instead of blindly enforcing compensation handlers.
* Guarantees that compensation functions receive validated identifiers to reverse database holds cleanly.
* Preserves all required skill structure and character limits in `scripts/verify_agent_os.py`.
