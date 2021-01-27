# Python assignment.
# 
# Instruction: Paint coverage.
# 
# Lecturer: Mr. Chizzy
# Course: CMS 112

def paint_coverage_calculator(available_paint_coverage, rLength, rWidth, rHeight, wHeight=0, wWidth=0): 
    room_perimeter = 2(rLength + wWidth)
    room_size = room_perimeter * rHeight

    room_size_without_windows = room_size - (wHeight + wWidth)
    paint_coverage = room_size_without_windows / available_paint_coverage

    return paint_coverage

# First Test Case: 
#       The room is 12 feet long, 10 feet wide and 8 feet tall.
first_paint_coverage = paint_coverage_calculator(100, 12, 10, 8)