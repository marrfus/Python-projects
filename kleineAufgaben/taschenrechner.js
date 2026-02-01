const rlSync = require('readline-sync'); //read was Mensch gedruckt hat
let a;
let b;
let ergebnis;


function plus(x, y) {
    return x + y;
}

function minus(x, y) {
    return x - y;
}

function mal(x, y) {
    return x * y;
}

function div(x, y) {
    if (y === 0) {
        console.log('Man darf nicht an 0 dividieren!');
        return "unmöglich";
    }
    return x / y;
}

function main() {
    //Hauptfunktion (läuft wenn das Program startet)

    // Fragt nach Zahlen und Aktion(Antwort ist String)
    a = rlSync.question('Lass uns rechnen! Gib mir bitte die erste Zahl.\n');
    b = rlSync.question('Gib mir bitte die zweite Zahl.\n');
    aktion = rlSync.question('Gib mir bitte die Aktion: + - * /\n');

    a = parseFloat(a);
    b = parseFloat(b);

    if (aktion === '+') {
        ergebnis = plus(a, b);
    };
    if (aktion === '-') {
        ergebnis = minus(a, b);
    };
    if (aktion === '*') {
        ergebnis = mal(a, b);
    };
    if (aktion === '/') {
        ergebnis = div(a, b);
    };

    console.log("Das Ergebnis von " + a + aktion + b + " ist " + ergebnis);
}

main();