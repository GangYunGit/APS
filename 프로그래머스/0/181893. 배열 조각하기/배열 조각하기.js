function solution(arr, query) {
    query.forEach((q, index) => {
        if (index % 2 === 0) {
            arr = arr.slice(0, q + 1)
        } else {
            arr = arr.slice(q, arr.length)
        }
    })
    return arr;
}