#!/usr/bin/env python3
"""Validate all UI-UX-V01 prompt sources and ledgers; standard library only."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]

def ck(cond,message):
    if not cond: raise RuntimeError(message)

def verify(part, expected, prefix):
    prompts=ROOT/part/'SCREEN_PROMPTS'
    files=sorted(prompts.glob('*.md'))
    ck(len(files)==expected, f'{part}: expected {expected} files, found {len(files)}')
    ledgerfile=ROOT/'tracking'/('admin_execution_ledger.json' if prefix=='ADM' else 'storefront_execution_ledger.json')
    ledger=json.loads(ledgerfile.read_text(encoding='utf-8'))
    ck(len(ledger)==expected, f'{part}: ledger length mismatch')
    ids=[e['id'] for e in ledger]
    routes=[e['route'] for e in ledger]
    paths=[e['source_file'] for e in ledger]
    ck(len(set(ids))==len(ids),f'{part}: duplicated IDs')
    if prefix == 'ADM':
        ck(len(set(routes))==len(routes),f'{part}: duplicated admin routes')
    else:
        # Storefront `/shop` intentionally has three distinct design states: home, mega-menu and mobile-home.
        from collections import Counter
        repeated={r:n for r,n in Counter(routes).items() if n>1}
        ck(repeated=={'/shop':3},f'{part}: unexpected duplicate storefront routes: {repeated}')
    ck(len(set(paths))==len(paths),f'{part}: duplicated paths')
    ck(all(e['id'].startswith(prefix+'-') for e in ledger),f'{part}: wrong ID prefix')
    ck({str(p.relative_to(ROOT)) for p in files}==set(paths),f'{part}: manifest vs prompt files mismatch')
    allowed={'PENDING','IN_PROGRESS','QA_FAILED','BLOCKED','COMPLETED'}
    for e in ledger:
        p=ROOT/e['source_file']
        t=p.read_text(encoding='utf-8')
        ck(e['id'] in t and 'PASTE INTO GOOGLE STITCH' in t, f'{p}: bad prompt or ID')
        ck(e['status'] in allowed, f'{e["id"]}: invalid status {e["status"]}')
        if e['status']=='COMPLETED':
            ck(bool(e['stitch_project_id'] and e['stitch_screen_id'] and e['stitch_screen_url']) and e['qa_status']=='PASSED',f'{e["id"]}: falsely marked COMPLETED')
    print(f'PASS {part}: {len(files)} prompts, {len(set(ids))} unique IDs, route states accounted for, ledger OK')

verify('02_ADMIN_PANEL',638,'ADM')
verify('01_STOREFRONT',122,'WEB')
count=len(list((ROOT/'02_ADMIN_PANEL'/'MODULE_PROMPTS').glob('*.md')))
ck(count==25, f'Expected 25 admin modules, got {count}')
print('PASS: 25 admin module documents, 760 distinct screens total.')
