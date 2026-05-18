import base64, os
from pathlib import Path
from openai import OpenAI

out = Path('assets/generated')
out.mkdir(parents=True, exist_ok=True)
client = OpenAI()
prompts = {
    'hero-cover.png': 'Editorial financial research cover image for an institutional investor brief titled "Top 10 AI Companies to Invest in — H2 2026". Aesthetic: Stratechery × PitchBook × a16z annual letter. Abstract AI infrastructure, semiconductor lattice, market data grids, calm serious tone, navy/charcoal background, restrained electric blue and amber accents, premium print publication, no readable small text except title if possible.',
    'company-profile-layout.png': 'High fidelity layout mockup for an AI company investment profile page. Include logo area placeholder, key metrics block, investment thesis section, risk callouts, valuation table, competitor comparison, H2 2026 catalysts. Institutional research deck style, clean grid, navy charcoal cream, electric blue accents, typography hierarchy, no real company logos.',
    'data-viz-style-frame.png': 'Data visualization style frame for an AI investment report: sample revenue growth line chart, funding rounds timeline, market share stacked bars, valuation multiples scatter. Premium financial research aesthetic, clear labels as generic placeholders, restrained palette navy charcoal cream electric blue amber green red.',
    'palette-typography.png': 'Color palette and typography pairing board for an institutional AI investment report. Show swatches: deep navy, graphite, warm ivory, electric blue, signal amber, risk red, growth green. Pair modern serif headline with neutral sans body, editorial finance design system, polished.'
}
for name, prompt in prompts.items():
    result = client.images.generate(model='gpt-image-2', prompt=prompt, size='1536x1024')
    img_b64 = result.data[0].b64_json
    (out/name).write_bytes(base64.b64decode(img_b64))
    print(f'wrote {out/name}')
