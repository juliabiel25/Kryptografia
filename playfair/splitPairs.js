let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

function matrixIndexOf(arr, val) {
    for(let i = 0; i < arr.length; i++) {
        let j = arr[i].indexOf(val);
        if (j != -1) {
            return [i, j];
        }
    }
    if (val == 'I') {
        return matrixIndexOf(arr, 'J');
    } else if (val == 'J') {
        return matrixIndexOf(arr, 'I');
    }
    return null;
}

function decodePlayfair(pairs, arr) {
    // decode pairs of characters
    let arrSize = arr.length;
    let decoded = '';
    for (let i = 0; i < pairs.length; i++) {
        let loc1 = matrixIndexOf(arr, pairs[i][0]);
        let loc2 = matrixIndexOf(arr, pairs[i][1]);
        let dec1, dec2;

        // on the same column
        if (loc1[1] == loc2[1]) {
            dec1 = arr[(loc1[0] - 1 + arrSize) % arrSize][loc1[1]];
            dec2 = arr[(loc2[0] - 1 + arrSize) % arrSize][loc2[1]];
        }
        // on the same row
        else if (loc1[0] == loc2[0]) {
            dec1 = arr[loc1[0]][(loc1[1] - 1 + arrSize) % arrSize];
            dec2 = arr[loc2[0]][(loc2[1] - 1 + arrSize) % arrSize];
        }
        // on a diagonal
        else {
            dec1 = arr[loc2[0]][loc1[1]];
            dec2 = arr[loc1[0]][loc2[1]];            
        }
        decoded += dec1 + dec2;
    }
    return decoded;    
}

function encodePlayfair(pairs, arr) {
    // encode pairs of characters
    let arrSize = arr.length;
    let encoded = '';
    for (let i = 0; i < pairs.length; i++) {
        let loc1 = matrixIndexOf(arr, pairs[i][0]);
        let loc2 = matrixIndexOf(arr, pairs[i][1]);
        let enc1, enc2;

        // on the same column
        if (loc1[1] == loc2[1]) {
            enc1 = arr[(loc1[0] + 1) % arrSize][loc1[1]];
            enc2 = arr[(loc2[0] + 1) % arrSize][loc2[1]];
        }
        // on the same row
        else if (loc1[0] == loc2[0]) {
            enc1 = arr[loc1[0]][(loc1[1] + 1) % arrSize];
            enc2 = arr[loc2[0]][(loc2[1] + 1) % arrSize];
        }
        // on a diagonal
        else {
            enc1 = arr[loc2[0]][loc1[1]];
            enc2 = arr[loc1[0]][loc2[1]];            
        }
        encoded += enc1 + enc2;
    }
    return encoded;    
}

function showCodingArray(arr) {
    const midSec = document.getElementById('middleSection');
    
    let section = document.createElement('section');
    section.setAttribute('class', 'optionGroup');
    section.setAttribute('id', 'codingArray');

    let h3 = document.createElement('h3');
    section.appendChild(h3);
    h3.innerHTML = 'Generated coding array';

    let table = document.createElement('table');
    for (let i in arr) {
        let row = document.createElement('tr');
        for (let j in arr[i]) {
            let cell = document.createElement('td');
            row.appendChild(cell);
            cell.innerHTML=arr[i][j];
        }
        table.appendChild(row);
    }
    section.appendChild(table);    
    midSec.appendChild(section);
}

function flushCodingArray() {
    const arr = document.getElementById('codingArray');
    if (arr) {
        document.getElementById('middleSection').removeChild(arr);
    }
}

function fillCodingArray(keyword) {
    const arrSize = 5;
    let arr = [];
    for (let i = 0; i < arrSize; i++) {
        arr.push([]);
        
        for (let j = 0; j < arrSize; j++) {
            let index = i * arrSize + j;
            
            // insert keyword
            if (index < keyword.length) {
                let char = keyword[index];
                arr[i].push(char)
                
                // delete from alphabet
                if (char == 'J' || char == 'I') {
                    alphabet = alphabet.replace(/[IJ]/g, '');
                    console.log("removing from the alphabet: J or I");
                } else {
                    alphabet = alphabet.replace(char, '');
                    console.log("removing from the alphabet: ", char);
                }
            }
            
            // insert remaining alphabet
            else if (index - keyword.length < alphabet.length) {
                arr[i].push(alphabet[index - keyword.length])
            }
            
            // insert 'X' in remaining spaces
            else {
                arr[i].push('X');
            }
        }
    }
    return arr;
}

function findDistinct(text) {
    let distinct = '';
    for (let i in text) {
        if (distinct.indexOf(text[i]) == -1) {
            distinct += text[i];
        }
    }
    return distinct;
}

// function splitReapeating(text, separator) {
//     let i = 1;
//     while (i < text.length) {
//         if (text[i - 1] == text[i]) {
//             text = text.substring(0, i) + separator + text.substring(i);
//             i += 2;
//         } else {
//             i++;
//         }
//     }
//     return text;
// }

function adjustText(text) {
    return text.toUpperCase().replace(/[^a-zA-Z]/g, '');
}

function makeEven(text) {
    return text.length%2 == 0 ? text : text + 'X'; 
}

function showWarnings(warnings) {
    console.log(warnings);
    const warningDiv = document.getElementById('warning');
    let warningMsg = "<b>Error</b>:<br>";
    for (let i in warnings) {
        warningMsg += warnings[i] + "<br>";
    }
    warningDiv.innerHTML = warningMsg;
    warningDiv.style.visibility = 'visible';
}

function flushWarnings() {
    const warningDiv = document.getElementById('warning');
    warningDiv.innerHTML = '';
    warningDiv.style.visibility = 'hidden';
}

function makePairs(text) {
    text = makeEven(text);
    let pairs = [];
    for (let i = 0; i < text.length-1; i+=2) {
        if (text[i] == text[i + 1]) {
            return i+1;
        } else {
            pairs.push(text[i] + text[i+1]);
        }
    }
    return pairs;
}

function onSubmit() {
    flushWarnings();
    flushCodingArray();
    let text = adjustText(document.getElementById('inputText').value);
    const encode = document.getElementById('fencode').checked;
    const decode = document.getElementById('fdecode').checked;
    let keyword =  adjustText(document.getElementById('fkeyword').value);
    let separator = document.getElementById('fseparator').value;
    
    // sprawdz czy poprawne dane
    let warnings = Array();
    if (!decode && !encode) {
        warnings.push("Neither 'encode' nor 'decode' was chosen.");
    }
    if (!keyword) {
        warnings.push("No keyword was given.");
    }
    if (separator.length != 1) {
        warnings.push("Separator should be 1 character long.")
    }

    if (warnings.length > 0) {
        showWarnings(warnings);
    } else if (text.length > 0) {
        keyword = findDistinct(keyword);
        let codingArray = fillCodingArray(keyword);
        showCodingArray(codingArray);

        // łączenie liter w pary
        // zwraca listę par albo index na którym należy wstawić separator
        let pairs = makePairs(text);
        let splits = 0;
        while (!isNaN(pairs)) {
            if (text[pairs] == separator) {
                warnings.push(`Infinite loop: '${separator}${separator}' can't be split by separator ${separator}`);
                showWarnings(warnings);
                break;
            }
            text = text.substring(0, pairs) + separator + text.substring(pairs);
            pairs = makePairs(text);
            splits++;
        } 
        console.log("Number of separator insertions: ", splits);
        console.log("input text after adjustments:\n", text);
        console.log("keyword after adjustments: ", keyword);

        const result = encode ? encodePlayfair(pairs, codingArray) : decodePlayfair(pairs, codingArray);
        document.getElementById('resultText').value = result;
    }    
}

// przerzucenie tekstu z prawej na lewą
function onSwap() {
    flushWarnings();
    flushCodingArray();
    const result = document.getElementById('resultText').value;
    document.getElementById('inputText').value = result;
    document.getElementById('resultText').value = '';
}