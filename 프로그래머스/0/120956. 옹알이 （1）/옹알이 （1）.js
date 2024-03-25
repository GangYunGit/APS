function solution(babbling) {
    let answer = 0;
    const talks = ["aya", "ye", "woo", "ma"];
    for (let word of babbling) {
        
        let checkWord = word;
        while (true) {
            for (let talk of talks) {
                if (word[0] === talk[0]) {
                    checkWord = word.replace(talk, "")
                    break
                }
            }
            if (word === checkWord) {
                break
            } else {
                word = checkWord
            } 
        }
        if (checkWord === "") {
            answer++
        }
        
    }
    return answer;
}