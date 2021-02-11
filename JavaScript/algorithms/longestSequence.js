const assert = require('assert');
const { parse } = require('path');

/**
 * Given a list of hands, get the longest sequence
 * Note: Ace can be both lo and hi card!
 */
const hands = [
    {
        hand: [{
            suit: 'Hearts',
            rank: 'Ace',
        },
        {
            suit: 'Hearts',
            rank: '2',
        },
        {
            suit: 'Hearts',
            rank: '3',
        },
        {
            suit: 'Diamonds',
            rank: 'Ace',
        }],
        length: 3
    },
    {
        hand: [{
            suit: 'Hearts',
            rank: 'Ace',
        },
        {
            suit: 'Hearts',
            rank: 'King',
        },
        {
            suit: 'Hearts',
            rank: 'Queen',
        },
        {
            suit: 'Hearts',
            rank: 'Jack',
        },
        {
            suit: 'Hearts',
            rank: '2',
        },
        {
            suit: 'Diamonds',
            rank: '3',
        }],
        length: 4
    },
    {
        hand: [{
            suit: 'Hearts',
            rank: 'Ace',
        },
        {
            suit: 'Hearts',
            rank: 'King',
        },
        {
            suit: 'Hearts',
            rank: 'Queen',
        },
        {
            suit: 'Hearts',
            rank: 'Jack',
        },
        {
            suit: 'Hearts',
            rank: '10',
        },
        {
            suit: 'Hearts',
            rank: '9',
        },
        {
            suit: 'Hearts',
            rank: '8',
        },
        {
            suit: 'Hearts',
            rank: '7',
        },
        {
            suit: 'Hearts',
            rank: '6',
        },
        {
            suit: 'Hearts',
            rank: '5',
        },
        {
            suit: 'Hearts',
            rank: '4',
        },
        {
            suit: 'Hearts',
            rank: '3',
        },
        {
            suit: 'Hearts',
            rank: '2',
        },],
        length: 13
    }
];

/**
 * 14 so we can handle the case were Ace can be before 2 and after King
 */
const CARDS_PER_SUIT = 14;

const getLongestSequence = (hand) => {
    const mp = {
        'Hearts': new Set(),
        'Spades': new Set(),
        'Diamonds': new Set(),
        'Clubs': new Set(),
    };

    const FaceCards = {
        'Ace': [1, 14],
        'King': 13,
        'Queen': 12,
        'Jack': 11,
    }

    hand.forEach(({suit, rank}) => {
        const parsedRank = parseInt(rank);
        const rankAsInt = Number.isInteger(parsedRank) ? parsedRank : FaceCards[rank];

        if (Array.isArray(rankAsInt)) {
            rankAsInt.forEach(r => mp[suit].add(r))
        } else {
            mp[suit].add(rankAsInt)
        }
    });

    let max = 0;
    Object.entries(mp).forEach(([_, cards]) => {
        // Handle case where the whole hand is the sequence
        if (cards.size === CARDS_PER_SUIT) {
            max = CARDS_PER_SUIT - 1;
            return;
        }

        cards.forEach(card =>{
            let i = card;
            let count = 1;
            while (i < CARDS_PER_SUIT && cards.has(i) && cards.has(i + 1)) {
                i += 1;
                count += 1;
            }
            max = Math.max(max, count);
        });
    });

    return max;

};

hands.forEach(({hand, length}, index) => {
    const res = getLongestSequence(hand);
    assert.strictEqual(
        res, length, 
        `Test case ${index} failed. Expected ${length}, got: ${res}`,
    );
})