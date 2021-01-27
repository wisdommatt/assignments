# Python assignment.
# 
# Instruction: Paint coverage.
# 
# Lecturer: Mr. Chizzy
# Course: CMS 112

def paint_coverage_calculator(available_paint_coverage, rLength, rWidth, rHeight, wHeight, wWidth): 
    room_perimeter = 2(rLength + wWidth)
    room_size = room_perimeter * rHeight

    room_size_without_windows = room_size - (wHeight + wWidth)
    