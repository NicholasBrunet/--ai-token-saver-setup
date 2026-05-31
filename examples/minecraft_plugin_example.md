# Few-Shot Example: Minecraft Plugin / Skript Hybrid

Prompt:

```text
I want generators to save like profiles.
```

Task:

```text
generator database persistence model dao sql migration api skript placed generator profile-like storage
```

Lessons:
- "like profiles" means inspect and reuse the profile persistence pattern.
- Skript-facing Java APIs must be null-safe.
- If a Java bridge class is missing, verify jar contents, package name, plugin load order, and full restart.
- If adding a DAO, update initialization wiring and API bridge.
- If migrations exist for multiple database flavors, update all flavors.
- If generated context is stale, rerun context generation instead of reading many files manually.
