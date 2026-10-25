"""Exact arithmetic for an invented A2 illustration, not an environment run."""
from decimal import Decimal as D
from pathlib import Path
import argparse
import json

def example():
    inputs = {
        'P': dict(temp='0.6', soc='0.2', imped='0.2', stress='0.8'),
        'Q': dict(temp='0.6', soc='0.8', imped='0.8', stress='0.7'),
    }
    rows = []
    for name, values in inputs.items():
        x = {k: D(v) for k, v in values.items()}
        assert all(D(0) <= value <= D(1) for value in x.values())
        simpler = x['temp'] + x['stress']**3
        product = D('0.5') * x['soc'] * x['imped']
        rows.append({'module': name, **values, 'simplerScore': f'{simpler:.3f}',
                     'addedProduct': f'{product:.3f}', 'a2Score': f'{simpler+product:.3f}'})
    p, q = rows
    assert (p['simplerScore'], q['simplerScore']) == ('1.112', '0.943')
    assert (p['a2Score'], q['a2Score']) == ('1.132', '1.263')
    differences = {key: f'{D(q[field])-D(p[field]):.3f}' for key, field in
                   [('simpler', 'simplerScore'), ('addedProduct', 'addedProduct'), ('a2', 'a2Score')]}
    assert differences == {'simpler': '-0.169', 'addedProduct': '0.300', 'a2': '0.131'}
    return {'status': 'invented normalized inputs; direct arithmetic only',
            'simplerExpression': 'temp+stress*stress*stress',
            'a2Expression': 'temp+(0.5*(soc*imped)+stress*stress*stress)',
            'rows': rows, 'QminusP': differences,
            'pairwiseChoices': {'simpler': 'P', 'A2': 'Q'},
            'limits': ['Scores are not rewards.', 'This is not a sampled trace or full four-module environment run.',
                       'The added product is supplied in H; both rules already contain cubic stress.',
                       'No better real-world action, safety, or source-domain causation is established.']}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(example(), indent=2) + '\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8', newline='\n')
    else:
        print(text, end='')
