// Rotate matrix
// Both O(n^2)

// O(n) space
function rotateMatrix(matrix: number[][]): number[][] {
  const rotated: number[][] = [];
  for (let i = 0; i < matrix.length; i++) {
    rotated[i] = new Array();
  }

  for (let x = 0; x < matrix.length; x++) {
    for (let y = 0; y < matrix[0].length; y++) {
      rotated[y][matrix[0].length - 1 - x] = matrix[x][y];
    }
  }

  return rotated;
}


function rotateMatrixByLayer(matrix: number[][]): number[][] {
  let top: number;
  let first: number;
  let last: number;
  let offset: number;

  for (let layer = 0; layer < matrix.length / 2; layer++) {
    first = layer;
    last = matrix.length - 1 - layer;
    
    for (let i = first; i < last; i++) {
      offset = i - first;
      top = matrix[first][i];

      matrix[first][i] = matrix[last - offset][first];
      matrix[last - offset][first] = matrix[last][last - offset];
      matrix[last][last - offset] = matrix[i][last];
      matrix[i][last] = top;
    }
  }

  return matrix;
}

const matrix: number[][] = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
];

console.log(
  'Rotate 90',
  matrix,
  '\n',
  rotateMatrixByLayer(matrix),
)