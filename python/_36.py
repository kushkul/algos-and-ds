class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def get_block_no(row, col):
            if row in [0,1,2]:
                if col in [0,1,2]:
                    return 0
                if col in [3,4,5]:
                    return 3
                if col in [6,7,8]:
                    return 6
            if row in [3,4,5]:
                if col in [0,1,2]:
                    return 1
                if col in [3,4,5]:
                    return 4
                if col in [6,7,8]:
                    return 7
            if row in [6,7,8]:
                if col in [0,1,2]:
                    return 2
                if col in [3,4,5]:
                    return 5
                if col in [6,7,8]:
                    return 8
          
                
        row_maps = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        col_maps = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        block_maps = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        
        for row_no, row_list in enumerate(board):
            for col_no, item in enumerate(row_list):
                if item == '.':
                    continue
                block_no = get_block_no(row_no, col_no)
                
                if item in row_maps[row_no].keys():
                    return False
                row_maps[row_no][item] = 1
                
                if item in col_maps[col_no].keys():
                    return False
                col_maps[col_no][item] = 1
                
                if item in block_maps[block_no].keys():
                    return False
                block_maps[block_no][item] = 1
        
        return True

