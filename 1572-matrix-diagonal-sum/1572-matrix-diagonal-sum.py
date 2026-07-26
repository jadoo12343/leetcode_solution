class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dim=len(mat)-1
        diag=0
        anti_diag=0
        i=0
        j=0
        while i<dim+1 and j<dim+1:
            if j==dim-j:
                diag+=mat[i][j]
            else:
                diag+=mat[i][j]
                anti_diag+=mat[i][dim-j]
            i+=1
            j+=1
        return diag+anti_diag
