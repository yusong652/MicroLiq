# Chapter 4 Remaining Issues (2026-02-18)

## Content Issues

### 1. Z_{m0} numerical inconsistency
- **Location**: Line ~315 vs Summary point (3)
- **Problem**: Main text says K₀=1.0 has Z_{m0} "approximately 5.0", but Summary gives the Dr80 range ceiling as 4.98 (actual value is 4.978)
- **Fix**: Change "approximately 5.0" to "approximately 4.98" in the main text, or round the Summary to 5.0

### 2. Towhata and Ishihara (1985) citation contradiction
- **Location**: Line ~263
- **Problem**: Cited for a "unique relationship between excess pore water pressure and shear work, despite differences in stress anisotropy." However, Fig. 4.12(b) shows the r_u-W_s curve for K₀=0.5 is clearly separated from K₀=1.0 and K₀=2.0, meaning the relationship is NOT unique across K₀ values
- **Fix**: Acknowledge the discrepancy, or clarify that the "uniqueness" in Towhata and Ishihara refers to a different context (e.g., different loading directions, not different K₀)

### 3. F_c defined but never used
- **Location**: Eq. (4-12) and Eq. (4-13), line ~329-331
- **Problem**: F_c is formally defined with two equations but is never plotted, tabulated, or referenced in results. The text immediately introduces α as a replacement. This creates a dead-end for the reader
- **Fix**: Either (a) add a brief sentence stating F_c was computed but is not shown because it lacks directional information, or (b) move the F_c definition to a brief remark rather than giving it full equation treatment

## Grammar / Language Issues

### 4. Line ~15: Tense inconsistency
- "These studies highlight the significance... and aroused great interest"
- **Fix**: "highlight...and have aroused" or "highlighted...and aroused"

### 5. Line ~19: Typo
- "applied both vertical and horizontal shear loading in to discuss"
- **Fix**: "in order to discuss" or simply "to discuss"

### 6. Line ~43: Extra space before comma
- "Table 4-2 ,where"
- **Fix**: "Table 4-2, where"

### 7. Line ~99: Non-standard article
- "The gravity was removed"
- **Fix**: "Gravity was removed"

### 8. Line ~333: Subject-verb disagreement
- "subtracts 1/3 from the diagonal elements of the fabric tensor and then multiplied by 15/2"
- **Fix**: "subtracts...and then multiplies by 15/2" or "...from which 1/3 is subtracted and then multiplied by 15/2"
