import os
from openpyxl import Workbook

# 掌握修改单元格尺寸

current_path = os.path.dirname(__file__)
output_path = os.path.join(current_path, 'Tutorial_Output')
save_path = os.path.join(output_path, 'tutorial06.xlsx')
os.makedirs(output_path, exist_ok=True)


wb = Workbook()
ws = wb.active

# adjust cell size
# ws.column_dimensions['C'].width = 100  # 列宽的单位是字符的宽度（基于默认字体）
# ws.row_dimensions[1].height = 100  # 行高的单位是点（point） 类似字体大小的单位

for col in ['A', 'B', 'C']:
    ws.column_dimensions[col].width = 40


# for row in range(1, 6):
#     ws.row_dimensions[row].height = 40

wb.save(save_path)