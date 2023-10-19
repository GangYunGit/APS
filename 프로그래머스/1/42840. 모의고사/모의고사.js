function solution(answers) {
    var answer = [];
    const p1 = [1, 2, 3, 4, 5]
    const p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    const p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    let scores = [{no : 1, score : 0}, {no : 2, score : 0}, {no : 3, score : 0}]
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] == p1[i % 5]) {
            scores[0].score ++;
        }
        if (answers[i] == p2[i % 8]) {
            scores[1].score ++;
        }
        if (answers[i] == p3[i % 10]) {
            scores[2].score ++;
        }
    }
    
    scores.sort((a, b) => b.score - a.score)
    const maxScore = scores[0].score
    
    scores.forEach((item) => {
        if (item.score === maxScore) {
            answer.push(item.no)
        }
    })
    
    return answer;
}