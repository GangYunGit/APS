function solution(arr1, arr2) {
    const arr1RowSize = arr1.length;
    const arr1ColSize = arr1[0].length;
    const arr2RowSize = arr2.length;
    const arr2ColSize = arr2[0].length;
    
    let answer = Array.from(Array(arr1RowSize), () => Array(arr2ColSize).fill(0))

    for (let i = 0; i < arr1RowSize; i++) {
        for (let j = 0; j < arr2ColSize; j++) {
            for (let k = 0; k < arr1ColSize; k++) {
                answer[i][j] += arr1[i][k] * arr2[k][j]
            }
        }
    }
    
    return answer;
}