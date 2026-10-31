# Baseline: direct Plugin invocation

Test prompt: package the existing skills without a default entry, then ask the
Plugin to process raw meeting notes completely and finish at Design Definition.

Observed behavior:

- The strongest trigger is `design-req-organizer`, so execution can stop after the
  Requirement Brief and AI Design Input.
- Continuing to `design-definition` depends on an unstated model assumption.
- Benchmarking is optional, but no shared entry defines when to insert it.
- The original capabilities remain independently discoverable.

The default entry must therefore define the default endpoint, benchmarking condition,
and independent-call override.
