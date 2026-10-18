# Implementation Plan: Toy Order Processor (Remediated — Aligned)

**Feature**: `003-toy-order-processor`  
**Stage**: `AG03 — Spec-Driven Drill`  
**Status**: `REMEDIATED & CONVERGED (ZERO CONTRADICTIONS)`  
**Date**: 2026-10-18  

---

## 1. Technical Stack & Architecture

* **Runtime Environment**: Node.js v22 (isolated TypeScript module).
* **Validation Layer**: Zod runtime schema validation for input contracts.
* **Component 1 (`OrderValidator`)**: Validates line items, positive unit prices, item quantities, and ISO 4217 currency.
* **Component 2 (`StateEngine`)**: Manages synchronous state transitions: `PENDING` $\rightarrow$ `CONFIRMED` or `REJECTED`.
* **Component 3 (`InMemoryOrderStore`)**: Stores orders in a private `Map<string, OrderRecord>` with atomic synchronous operations.
* **Component 4 (`IdempotencyManager`)**: Stores request keys in `Map<string, { response: OrderResponse, expiresAt: number }>` with 60-second TTL eviction.

---

## 2. In-Memory Data Storage Architecture

```typescript
export interface OrderRecord {
  id: string;
  items: Array<{ sku: string; quantity: number; unitPrice: number }>;
  currency: "SAR" | "USD";
  totalAmount: number;
  status: "CONFIRMED" | "REJECTED";
  createdAt: Date;
}

export class InMemoryOrderStore {
  private orders = new Map<string, OrderRecord>();

  public save(order: OrderRecord): void {
    this.orders.set(order.id, { ...order });
  }

  public getById(id: string): OrderRecord | undefined {
    return this.orders.get(id);
  }
}

export class IdempotencyManager {
  private cache = new Map<string, { response: any; expiresAt: number }>();
  private readonly ttlMs = 60_000; // 60 seconds

  public get(key: string): any | null {
    const entry = this.cache.get(key);
    if (!entry) return null;
    if (Date.now() > entry.expiresAt) {
      this.cache.delete(key);
      return null;
    }
    return entry.response;
  }

  public set(key: string, response: any): void {
    this.cache.set(key, { response, expiresAt: Date.now() + this.ttlMs });
  }
}
```

---

## 3. Execution Phases

1. **Phase 1: Contracts & Validation**: Define TypeScript interfaces, Zod schema, and `OrderValidator`.
2. **Phase 2: In-Memory Storage**: Implement `InMemoryOrderStore` and `StateEngine`.
3. **Phase 3: Idempotency Subsystem**: Implement `IdempotencyManager` with 60s TTL eviction.
4. **Phase 4: Main Service Pipeline**: Compose validator, state engine, store, and idempotency into `processOrder()`.
5. **Phase 5: Automated Test Harness**: Implement unit, negative, and latency benchmarking tests covering AC-01 through AC-04.
