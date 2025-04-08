const stream = [
    'host:a,role:web,availability-zone:us-east-a1',
    'host:b,role:web,availability-zone:us-east-ab',
    'host:a,role:web,availability-zone:us-east-a1',
    'host:c,role:master,availability-zone:us-east-1e',
    'host:d,role:replica,availability-zone:us-east-1a',
    'host:d,role:replica,availability-zone:us-east-1a',
]

const output = {
    'availability-zone:us-east-a1': 2,
    'availability-zone:us-east-ab': 1,
    'availability-zone:us-east-1e': 1,
    'availability-zone:us-east-1a': 2,
    'host:a': 2,
    'host:b': 1,
    'host:c': 1,
    'host:d': 2,
    'role:web': 3,
    'role:master': 1,
    'role:replica': 2,
}


const solution = (input) => {
    const result = new Map();
    for(let i = 0; i < input.length; i++) {
        const words = input[i].split(",");
        for(const word of words) {
            result.set(word, result.get(word) ?? result.get(word)++);
        }
    }
    return result
}

console.log(output === solution(stream));