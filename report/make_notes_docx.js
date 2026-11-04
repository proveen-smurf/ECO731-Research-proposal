// Builds report/meeting_notes.docx (short meeting notes for the professor).
// Run from the repo root:  NODE_PATH=<dir with docx installed> node report/make_notes_docx.js
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, LevelFormat,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, ImageRun,
} = require('docx');

const FONT = 'Arial';
const t = (text, o = {}) => new TextRun({ text, font: FONT, ...o });
const p = (runs, o = {}) => new Paragraph({ children: Array.isArray(runs) ? runs : [t(runs)], spacing: { after: 100 }, ...o });
const h1 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [t(text)] });
const bullet = (runs, level = 0) => new Paragraph({
  numbering: { reference: 'bullets', level },
  children: Array.isArray(runs) ? runs : [t(runs)], spacing: { after: 60 },
});
const num = (runs, ref = 'numbers') => new Paragraph({
  numbering: { reference: ref, level: 0 },
  children: Array.isArray(runs) ? runs : [t(runs)], spacing: { after: 80 },
});
const b = (text) => t(text, { bold: true });
const i = (text) => t(text, { italics: true });

// Versions table
const W = [1900, 2900, 4838];
const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: border, bottom: border, left: border, right: border };
const cell = (text, w, head = false) => new TableCell({
  width: { size: w, type: WidthType.DXA }, borders,
  shading: head ? { type: ShadingType.CLEAR, color: 'auto', fill: 'E7F1FB' } : undefined,
  margins: { top: 60, bottom: 60, left: 100, right: 100 },
  children: [new Paragraph({ children: [t(text, { bold: head, size: 19 })] })],
});
const rows = [
  ['Version', 'What it adds', 'Main finding'],
  ['1. Two periods', 'Turnover (q) and raiding (φ)', 'Save only if expected raiding (1−q)φ is below the patience gap (about 0.8%).'],
  ['2. Rival successor', 'Next government values different spending', 'Three regimes: borrow, balanced budget, save. The middle band exists only because of raiding.'],
  ['3. Infinite horizon', 'Markov equilibrium, solved numerically', 'The band survives. Showed I need the Battaglini–Coate benchmark (patience = interest rate, plus shocks).'],
  ['4. Spending shocks', 'Buffer (precautionary) motive', 'Tolerable turnover risk ≈ ε(1+2ε)σ²/φ. Buffer benefit is second order, raiding cost first order.'],
  ['5. Protected fund', 'Fund is ring-fenced, but borrowing can offset it', 'Protection only works if the borrowing limit is tight.'],
  ['6. Long run (latest)', 'Infinite horizon + shocks + raiding', 'Raiding removes the long-run anchor; a debt ceiling must bind.'],
];
const table = new Table({
  width: { size: W.reduce((a, c) => a + c, 0), type: WidthType.DXA },
  columnWidths: W,
  rows: rows.map((r, k) => new TableRow({ tableHeader: k === 0, children: r.map((c, j) => cell(c, W[j], k === 0)) })),
});

const fig = new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 120, after: 60 },
  children: [new ImageRun({ type: 'png', data: fs.readFileSync('report/fig_v6_longrun.png'),
    transformation: { width: 480, height: 181 },
    altText: { title: 'Long-run debt', description: 'Mean debt and share of paths holding a fund over 6000 periods: planner vs raiding', name: 'fig' } })],
});

const children = [
  new Paragraph({ heading: HeadingLevel.TITLE, children: [t('Why don’t governments build funds?')] }),
  p([i('Research notes for our meeting — 4 November 2026')], { spacing: { after: 200 } }),

  h1('The question'),
  bullet('In the planner benchmark (Battaglini & Coate 2008), the government saves until the interest pays for spending, and taxes are zero forever.'),
  bullet('Real governments almost never do this. Indian states carry heavy debt and only small sinking funds.'),
  bullet('Why not, and what would let them build a fund?'),

  h1('The idea'),
  bullet([t('The incumbent may lose office (probability 1 − q), and the next government can grab part '), b('φ'), t(' of any fund.')]),
  bullet('So a rupee saved is worth less to the incumbent than to a planner.'),
  bullet('Different from Battaglini–Coate’s pork: their waste happens every period whoever governs; mine only hits the stock of savings when power changes hands. A government sure to stay in office saves like the planner.'),

  h1('What I’ve built so far'),
  table,
  p('', { spacing: { after: 60 } }),

  h1('Main results'),
  num([b('Small raiding risk is enough to stop saving. '), t('The benefit of a buffer fund grows with the square of spending volatility; the cost of raiding grows with φ itself. With realistic numbers, a turnover risk above roughly 1–3% means no fund.')]),
  num([b('Raiding creates a “do nothing” zone. '), t('Turnover plus a rival with different priorities gives debt; raiding blocks saving but can’t create debt on its own, so in between governments just balance the budget.')]),
  num([b('More volatile spending helps saving. '), t('States facing bigger shocks can tolerate more turnover risk and still save.')]),
  num([b('Protecting the fund isn’t enough on its own. '), t('A successor can borrow against a ring-fenced fund. Protection works only together with a tight borrowing limit: they are complements.')]),
  num([b('Latest: raiding removes the long-run anchor. '), t('For the planner, the zero-tax fund is where the economy settles. I can prove that with any raiding risk (even a 0.1% expected loss a year):')]),
  bullet('there is no steady state: funds disappear and debt keeps wandering;', 1),
  bullet('with a debt ceiling, a steady state exists, and the ceiling must bind some of the time;', 1),
  bullet('on average the ceiling exactly offsets the raiding distortion, and how often a fund can be held is capped by the ceiling’s bite divided by (1 − q)φ.', 1),

  h1('Rough idea of the proof'),
  bullet([t('Track the cost of raising one more rupee of tax (MCPF). With raiding it can only drift '), b('up'), t(' on average: when holding a fund, the government discounts the raided outcome, but that outcome still happens.')]),
  bullet('In a steady state the average drift must be zero, so no fund is ever held and the MCPF becomes a “fair game”.'),
  bullet('A fair game with a floor eventually freezes, which means constant taxes forever. But then every spending shock piles into debt without limit. Contradiction.'),
  bullet('With a ceiling, the ceiling provides the downward push, so a steady state can exist, but only if it binds.'),
  bullet('Same method as Chamberlain & Wilson (2000), applied to raided public funds. Simulations confirm it (below).'),
  fig,
  p([i('Planner (grey) builds a fund; with raiding (blue) funds vanish and debt drifts up. A 0.1% expected loss (dashed) behaves almost like 3%.')], { alignment: AlignmentType.CENTER, spacing: { after: 160 } }),

  h1('Link to India'),
  bullet('State sinking funds (CSF) are ring-fenced at the RBI, but nothing ties borrowing to them; borrowing is capped by the Centre’s net borrowing ceiling (about 3% of GSDP).'),
  bullet('The model predicts small funds and borrowing ceilings that bind regularly. That seems to fit what we see, and is worth checking with data.'),
  bullet('Open point: if the CSF repays maturing loans, it may free up borrowing room. Then the CSF withdrawal rule is the real φ.'),

  h1('Next step: making re-election depend on policy'),
  p('Following Lindbeck & Weibull (1987), re-election chances q would fall when taxes are high. What changes depends on why the incumbent cares about winning:'),
  bullet([b('Option A – the government only cares about citizens. '), t('Winning matters only because losing means the fund is raided. Saving now has an electoral cost (higher taxes today make the fund less safe), but only once a fund exists; debt is unaffected. Results get stronger, and the proofs mostly carry over. Small extension.')]),
  bullet([b('Option B – politicians also value being in office. '), t('Borrowing before elections to cut taxes wins votes: political budget cycles, as in Khemani (2004) for Indian states. More debt, and ceilings bind even more often. But the government is no longer “one planner in disguise”, so the proofs need a new strategic analysis (Battaglini 2014). Large; a paper in itself.')]),

  h1('What I’d like your view on'),
  num('Is the Battaglini–Coate benchmark (patience = interest rate, raided money simply lost) fine as the main setting?', 'q'),
  num('Is the long-run result a contribution worth building the paper around?', 'q'),
  num('Which is worth going forward with: Option A (quick, keeps the proofs) or Option B (political budget cycles, closer to India, much harder)? Or first add the rival-priorities successor to the long-run model?', 'q'),
  num('Worth taking to Indian state data (use of borrowing ceilings, CSF balances)?', 'q'),

  p([i('Derivations were checked and the simulations coded with help from Claude (an AI assistant). Full proofs and code are available.')], { spacing: { before: 200 } }),
];

const doc = new Document({
  creator: 'ECO731 project',
  title: 'Research notes',
  styles: {
    default: { document: { run: { font: FONT, size: 20 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', next: 'Normal', run: { font: FONT, size: 36, bold: true, color: '1F3864' }, paragraph: { spacing: { before: 0, after: 60 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 26, bold: true, color: '1F3864' }, paragraph: { spacing: { before: 220, after: 80 }, keepNext: true, outlineLevel: 0 } },
    ],
  },
  numbering: {
    config: [
      { reference: 'bullets', levels: [
        { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } },
        { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 900, hanging: 260 } } } },
      ] },
      { reference: 'numbers', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 300 } } } }] },
      { reference: 'q', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 300 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 850, bottom: 850, left: 1000, right: 1000 } } },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync('report/meeting_notes.docx', buf);
  console.log('written report/meeting_notes.docx');
});
