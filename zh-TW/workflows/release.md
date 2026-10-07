# Release Workflow

```text
Select Release Scope
  -> Validate
  -> Documentation Sync
  -> Repository Review
  -> Build Artifact
  -> Verify Artifact
  -> Pre-release Gate
  -> Tag / Publish
  -> Final Record
```

1. **Select Release Scope**：確認版本、包含的 Commit、Breaking change 與 Compatibility，依 `REL-001`、`REL-002`。
2. **Validate**：執行適用的 Validation Level 與 regression 檢查。
3. **Documentation Sync**：依 Documentation Rules 更新 README、Usage、Config、Migration 與 Release notes。
4. **Repository Review**：依 Git Rules 確認 Branch、Diff、Secrets、Runtime data 與預計發布 Commit。
5. **Build Artifact**：建立實際發布內容。
6. **Verify Artifact**：依 `REL-004`、`REL-005` 驗證打包後內容。
7. **Pre-release Gate**：通過 `gates/pre-release.md`。
8. **Tag / Publish**：依 `REL-007` 與 Decision Rules 執行外部發布。
9. **Final Record**：重大 Release 可使用 `templates/work-record.md` 留下目的、變更、驗證與 Known limitations。
