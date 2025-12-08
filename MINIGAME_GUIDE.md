# UNDERTALE-STYLE COMBAT MINIGAME GUIDE

## Overview

TERMINAL.EXIT uses an UNDERTALE-inspired timing-based attack system. Instead of selecting "high damage" or "low damage," you must demonstrate your reflexes by hitting the strike zone at the right moment.

## How the Minigame Works

### Visual Display

```
Strike Zone: [--------#####-----]

Where:
- `-` = Safe zone (no damage/miss area)
- `#` = Strike zone (hit area)
- `|` = Your cursor (moves continuously)
```

### Game Flow

1. **Setup Phase:** Strike zone is displayed
2. **Cursor Phase:** A cursor `|` moves left-right continuously
3. **Input Phase:** You press SPACE/ENTER when cursor enters the zone
4. **Result:**
   - **HIT** (cursor in zone): Critical damage (10-16 HP base)
   - **MISS** (cursor outside zone): Glancing blow (1-4 HP)

### Difficulty Levels

The cursor moves at constant speed across the bar. Timing is precise but learnable:

- **Beginner:** Very wide zone (easier to hit)
- **Normal:** Standard 5-block zone (challenging)
- **Hard:** Very narrow 3-block zone (requires precision)

## Upgradeable Strike Zones

Your AI companion can receive modules that modify the strike zone:

### Base Configuration (No Upgrades)
```
Strike Zone: [--------#####-----]
Size: 5 blocks
Base Damage: 10-16 HP
```

### Precision Module (When Found)
```
Strike Zone: [-----########------]
Size: 8 blocks
Base Damage: 10-16 HP
Effect: Larger zone = Easier to land hits
Color: ORANGE
```

### Rapid Attack Module (When Found)
```
Strike Zone: [----------###-------]
Size: 3 blocks
Base Damage: 13-19 HP (+3 bonus)
Effect: Smaller zone = More damage if you can hit it
Color: BLUE
```

### Power Module (When Found)
```
Strike Zone: [--------#####-----]
Size: 5 blocks
Base Damage: 15-21 HP (+5 bonus)
Effect: Hits harder overall
Color: RED
```

## Strategy Guide

### Against Different Enemies

**Glitched Sentinel (First Fight)**
- Simple, predictable patterns
- Good for learning the minigame
- Recommended: Normal difficulty zone
- Strategy: Build rhythm, nail a few hits in a row

**Data Phantom (Medium)**
- Fast, confusing
- Recommended: Precision Module if available
- Strategy: Use AI Analyze for hints between attacks

**Corrupted Fragment (Hard)**
- Small, quick
- Recommended: Rapid Attack Module for bonus damage
- Strategy: Quick precise hits, don't hesitate

**System Echo (Boss)**
- Strongest, mirrors your moves
- Recommended: Power Module + Mercy path
- Strategy: Consider mercy instead of pure damage

## Tips for Success

### Timing Tips
1. **Watch the cursor path:** It moves in a smooth left-to-right pattern
2. **Anticipate the zone:** Don't wait until cursor reaches zone, prepare to hit
3. **Consistent rhythm:** Try to maintain steady timing across multiple rounds
4. **Don't panic:** Missing is okay, just hit the next zone

### Damage Optimization
- **Critical Hit:** Strike exactly in center of zone = highest damage
- **Partial Hit:** Strike at edge of zone = lower damage
- **Miss:** Strike outside = minimal damage

### Combo Strategy
- Build confidence with early hits
- The more you hit, the better your timing gets
- After 3-4 hits, you'll find the zone's "feel"
- Use Analyze button to break rhythm if needed

## Upgrade Path Recommendations

### For Beginners
1. **First:** Find Precision Module (larger zone)
2. **Second:** Find Power Module (+damage)
3. Result: Easier hits + higher damage

### For Skilled Players
1. **First:** Find Power Module (+damage)
2. **Second:** Find Rapid Attack Module (challenge mode)
3. Result: Hard but rewarding - massive damage

### For Speedrunners
1. **Only:** Rapid Attack Module (3-block zone)
2. Result: Super tight timing = instant victories

## Advanced Mechanics (Future)

### Planned Module Effects

**Burn Module (RED)**
- Hits apply burning damage
- Enemy takes 2 damage per turn
- Strike Zone: Standard 5 blocks

**Parry Module (SILVER)**
- 30% chance to dodge incoming attacks
- Replaces one hit of enemy damage with dodge animation
- Strike Zone: Standard 5 blocks

**Focus Module (YELLOW)**
- Analyze button gives hints about enemy pattern
- Next hit gets +2 damage if you follow hint
- Strike Zone: Standard 5 blocks

**Bloodlust Module (DARK RED)**
- Each hit increases damage by +1 (stacks)
- Reset if you miss
- Strike Zone: Standard 5 blocks

## Common Mistakes to Avoid

❌ **Waiting for zone instead of predicting:** You'll be too late  
✅ **Predict zone location, press early:** Time it right

❌ **Panicking on first miss:** Missing is normal  
✅ **Stay calm, hit next zone cleanly**

❌ **Not using Analyze when confused:** You have free actions  
✅ **Use Analyze to break up attack attempts**

❌ **Ignoring upgrades:** They matter!  
✅ **Always pick up new modules

## Example Perfect Run

```
Turn 1: [Minigame] HIT in zone center → 15 damage
Turn 2: [Minigame] HIT in zone → 12 damage
Turn 3: [AI Analyze] Enemy HP: 13 remaining
Turn 4: [Minigame] HIT in zone center → 13 damage
Turn 5: Enemy defeated!

Total: 40 damage in 4 action turns
```

## Example Bad Run

```
Turn 1: [Minigame] MISS → 2 damage
Turn 2: [Minigame] MISS → 1 damage
Turn 3: [AI Analyze] Enemy pattern revealed
Turn 4: [Minigame] HIT! → 12 damage
Turn 5: [Use Potion] Heal 30 HP
Turn 6: [Minigame] HIT! → 14 damage
...
(Takes many turns)
```

## Difficulty Progression

| Enemy | HP | Zone Size | Strategy |
|-------|----|-----------| ---------|
| Glitch | 30 | 5 blocks | Learn timing |
| Phantom | 25 | 5 blocks | Use Analyze |
| Fragment | 20 | 5 blocks | Quick hits |
| Echo | 35 | 5 blocks | Consider Mercy |

## Pro Tips

🎯 **Zone Prediction:** After 2 hits, you'll know exactly when to press  
⚡ **Speed Over Power:** Fast weak hits > slow strong hit attempts  
🧠 **AI Integration:** Use Analyze strategically, not just for damage  
💚 **Item Management:** Save potions for boss fight (Echo)  
🤝 **Mercy Path:** Consider sparing enemies you've struggled with  

---

**Master the minigame, defeat the system, escape with your AI companion.**
