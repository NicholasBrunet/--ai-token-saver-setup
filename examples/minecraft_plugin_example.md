# Few-Shot Example: Minecraft Plugin / Skript Hybrid

## Repository Traits

This repository may include:

- Java/Paper plugin source
- Skript scripts
- skript-reflect bridge classes
- plugin.yml load order
- database models/DAOs
- SQL migrations
- server runtime folders
- generated remap/plugin cache folders

## Example Pattern: Profile Persistence

A profile persistence system may follow:

```text
Profile.java
→ ProfileDao.java
→ V1__initial.sql
→ SkDatabaseAPI.java
→ Profile.sk
→ commands/events
```

## Example Prompt

```text
I want generators to save like profiles.
```

## Correct Interpretation

Do not ask the user to explain "profiles."

Interpret as:

```text
generator database persistence model dao sql migration api skript placed generator profile-like storage
```

## Example Route

```json
{
  "route_name": "generator_database_persistence",
  "description": "Adds or modifies database-backed placed-generator persistence by mirroring the profile persistence pattern.",
  "match_terms": [
    "generator",
    "placed generator",
    "save like profiles",
    "database persisted",
    "move generator data into database"
  ],
  "negative_match_terms": [],
  "task_terms": "generator database persistence model dao sql migration api skript placed generator profile-like storage",
  "recommended_scope": "mixed-plugin-and-skript",
  "include_paths": [
    "BanknoteLib",
    "dev-server/plugins/Skript/scripts/generators",
    "dev-server/plugins/Skript/scripts/core",
    "dev-server/plugins/Skript/scripts/data"
  ],
  "avoid_paths": [
    "dev-server/world",
    "dev-server/world_nether",
    "dev-server/world_the_end",
    "dev-server/libraries",
    "dev-server/versions",
    "dev-server/cache",
    "dev-server/plugins/.paper-remapped"
  ],
  "related_systems": [
    "profile persistence",
    "generator scripts",
    "skript java bridge"
  ],
  "validation_commands": [
    "./gradlew build"
  ],
  "known_pitfalls": [
    "Skript-facing Java APIs must be null-safe.",
    "Plugin jars must be rebuilt and copied before testing classloader changes.",
    "Do not use /reload for plugin classloader changes.",
    "If a Java bridge class is not found, verify jar contents and plugin load order.",
    "If adding a DAO, update plugin initialization and public API wiring.",
    "If adding migrations, update every supported database flavor."
  ],
  "confidence": 0.9
}
```

## Lessons

- Always report full relative paths.
- Build success does not mean the server is using the new jar.
- If Skript cannot find a class, check jar contents, package name, plugin load order, and full restart.
- If a compiler error names one exact file, still use a narrow workflow and validate.
- For broad persistence migrations, make a foundation pass first.
