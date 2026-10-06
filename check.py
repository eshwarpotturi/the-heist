"""Verify the hand-written numbers in docs/take.js against docs/matches.json."""
import json
M=json.load(open('docs/matches.json'))['matches']
ref=lambda m: any(t.get('aborted') for t in m['turns'])
assert len(M)==27
assert sum(1 for m in M for t in m['turns'] if t['thief']['message'])==240
assert sum(m['parts'] for m in M)==0
assert sum(t['leak']['name'] or t['leak']['price'] for m in M for t in m['turns'])==0
assert sum(ref(m) for m in M if m['thief']=='haiku')==3 and sum(ref(m) for m in M)==3
assert sum(1 for m in M if m['thief']=='haiku')==9
print('all headline numbers match the data')
