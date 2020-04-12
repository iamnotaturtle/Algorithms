// Zero matrix

function zeroMatrix(matrix: number[][]): number[][] {
  
  // Check first row/column for zeroes
  let isRowZero = false;
  let isColumnZero = false;

  for (let i = 0; i < matrix.length; i++) {
    if (matrix[0][i] === 0) {
      isRowZero = true;
      break;
    }
  }

  for (let i = 0; i < matrix[0].length; i++) {
    if (matrix[i][0] === 0) {
      isColumnZero = true;
      break;
    }
  }

  for (let i = 1; i < matrix.length; i++) {
    for (let j = 1; j < matrix[0].length; j++) {
      if (matrix[i][j] === 0) {
        matrix[0][j] = 0;
        matrix[i][0] = 0;
      }
    }
  }

  for (let i = 0; i < matrix[0].length; i++) {
    if (matrix[0][i] === 0) {
      nullifyColumn(matrix, i);
    }
  }

  for (let i = 0; i < matrix.length; i++) {
    if (matrix[i][0] === 0) {
      nullifyRow(matrix, i);
    }
  }

  if (isRowZero) {
    nullifyRow(matrix, 0);
  }

  if (isColumnZero) {
    nullifyColumn(matrix, 0);
  }

  return matrix;
}

function nullifyRow(matrix: number[][], row: number): number[][] {
  for (let i = 0; i < matrix[0].length; i++) {
    matrix[row][i] = 0;
  }
  return matrix;
}

function nullifyColumn(matrix: number[][], column: number): number[][] {
  for (let i = 0; i < matrix.length; i++) {
    matrix[i][column] = 0;
  }
  return matrix;
}

const test: number[][] = [
  [1, 2, 3, 4],
  [5, 6, 7, 0],
  [0, 10, 11, 12],
  [13, 14, 15, 16],
];

const small = [
  [1, 2],
  [0, 4],
]

console.log(
  `Zero Matrix`,
  zeroMatrix(test),
);