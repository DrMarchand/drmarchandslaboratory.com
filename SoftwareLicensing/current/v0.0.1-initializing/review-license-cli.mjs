/*
 * File rights: copyright holder pending work-specific verification.
 * Read-only software license advisory. No license grant or approval.
 */
import { createInterface } from 'node:readline/promises';
import { stdin, stdout } from 'node:process';
import { recommendLicense } from './recommend-license.mjs';

const fields = [
  ['artifactKind', 'Artifact type', ['software_only', 'mixed_assets', 'artwork_only'], 'software_only'],
  ['softwarePurpose', 'Purpose', ['language_or_engine', 'sdk_or_api', 'small_utility', 'simple_library', 'other'], 'other'],
  ['distribution', 'Intended distribution', ['public_release', 'client_delivery', 'internal_only'], 'internal_only'],
  ['patentConcern', 'Patent concern', ['material', 'low', 'unknown'], 'unknown'],
  ['contributors', 'Contributor provenance', ['multiple', 'single', 'unknown'], 'unknown'],
  ['rightsStatus', 'Work-specific rights verification', ['verified', 'pending', 'disputed'], 'pending'],
  ['dependencyStatus', 'Dependency license inventory', ['cleared', 'unknown', 'incompatible'], 'unknown'],
  ['existingLicense', 'Existing license', ['none', 'MIT', 'Apache-2.0', 'other', 'unknown'], 'unknown'],
  ['restrictionGoal', 'Requested business restriction', ['none', 'noncommercial', 'no_derivatives', 'exclusive'], 'none']
];
const rl = createInterface({ input: stdin, output: stdout });
async function choose(label, options, fallback = null) {
  stdout.write('\n' + label + '\n');
  options.forEach((x, i) => stdout.write(' ' + (i + 1) + '. ' + x + '\n'));
  const hint = fallback ? ' [default: ' + fallback + ']' : '';
  while (true) {
    const raw = (await rl.question('Choice 1-' + options.length + hint + ': ')).trim();
    if (!raw && fallback != null) return fallback;
    const i = Number(raw);
    if (/^[0-9]+$/.test(raw) && Number.isInteger(i) && i >= 1 && i <= options.length) return options[i-1];
    stdout.write('Choose one of the numbered options.\n');
  }
}

try {
  stdout.write('DESIGN ORCHARD SOFTWARE LICENSE REVIEW (DRAFT)\n');
  stdout.write('No licensing, file changes, uploads, or approval will occur.\n');
  const input = {};
  for (const [key, label, values, fallback] of fields) {
    input[key] = await choose(label, values, fallback);
  }
  let result = recommendLicense(input);
  stdout.write('\nRecommendation: ' + (result.recommendation || 'none') + '\n');
  for (const reason of result.reasons) stdout.write('  Why: ' + reason + '\n');
  stdout.write('Review flags: ' + result.flags.length + ', blockers: ' + result.blockingCodes.length + '\n');
  for (const f of result.flags) stdout.write('  [' + f.severity + '] ' + f.code + ': ' + f.explanation + '\n');

  input.selectedLicense = await choose('Tentative human selection (NOT an approval)', [
    'No selection', 'Apache-2.0', 'MIT'
  ], 'No selection');
  if (input.selectedLicense === 'No selection') input.selectedLicense = null;
  result = recommendLicense(input);
  stdout.write('\nSelected: ' + (result.selectedLicense || 'none') + '\n');
  stdout.write('Recommended: ' + (result.recommendation || 'none') + '\n');
  stdout.write('Blocking issues: ' + (result.blockingCodes.join(', ') || 'none detected by this limited policy') + '\n');
  stdout.write('Decision: human_review_required | applicationAllowed=false | releaseAuthorized=false\n');
  for (const f of result.flags.filter(x => x.code === 'OVERRIDE_REQUIRES_RATIONALE')) {
    stdout.write('Override requires written rationale: ' + f.explanation + '\n');
  }
} finally {
  rl.close();
}
