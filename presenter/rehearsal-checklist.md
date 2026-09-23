# Rehearsal and publication gates

## Rehearse

- [ ] Choose exact Glyphs, app, sidecar, bridge, skills and client versions.
- [ ] Verify installation on a fresh participant-like Mac/account.
- [ ] Validate each advertised client separately; resolve ChatGPT instructions.
- [ ] Time all three exercises, including participant pauses.
- [ ] Inspect source and path; prove read-only inspection leaves the font unchanged.
- [ ] Prove preview leaves H at 600; apply makes H 620 and leaves O at 600.
- [ ] Prove workflow undo restores H to 600 without changes elsewhere.
- [ ] Prove script selection, empty selection and no-font behavior in Glyphs 4.
- [ ] Capture final-build setup, connection, before/after/restored screens.
- [ ] Record and verify short fallback videos; store separately.
- [ ] Agree final agenda with Rainer.

## Publish only with the owner's explicit approval

- [ ] Audit all repository history and assets for secrets/private fonts/paths.
- [ ] Review licenses, notices, speaker details, wording and timezone labels.
- [ ] Freeze a workshop revision; build the participant ZIP and SHA256SUMS.
- [ ] Make the repository public (not automated by this project).
- [ ] Download the exact public codeload commit archive and compute its SHA-256.
- [ ] Create a schemaVersion 1 registry entry: id, name, description, author,
      license, repository, templateDirectory="template", 40-character revision,
      and archiveSHA256. Hash the codeload archive, NOT the participant ZIP.
- [ ] Publish the registry update through the main project's normal review path.
- [ ] Refresh Templates in the app and verify download/create from a clean cache.
- [ ] Confirm all participant links work signed out.
- [ ] Copy the approved workshop page into the public website; keep it unlisted
      if desired. Removing navigation does not make a published page private.

No scripts here change visibility, invite collaborators or publish the registry.
