"""Phase 2+3: Consolidate to target stress and stabilize.

Restores a void-ratio state, ramps to target isotropic stress,
then stabilizes with tight tolerance.

Usage in PFC IPython console:
    %run consolidation/consolidate_stress.py
"""

from consolidate import ConsolidationServo, TARGET_STRESS

import itasca as it


# ── Configuration ─────────────────────────────────────────────

# Which void ratio state to process (must have comp_e_XXX saved)
VOID_RATIO = 0.655


# ── Main ──────────────────────────────────────────────────────

if __name__ == '__main__':
    it.command("model restore 'comp_e_%.3f'" % VOID_RATIO)
    servo = ConsolidationServo()

    def servo_callback():
        servo.cycle()

    servo.consolidate_to_stress(TARGET_STRESS)
    servo.stabilize(TARGET_STRESS)
    print("=== Specimen e=%.3f complete ===" % VOID_RATIO)
