import { create } from 'zustand'

type Store = {
    level: number,
    hp: number;
    maxHp: number;
    attack: number;
    exp: number;
    gold: number;
    enemy: Enemy | null;
    setEnemy: (enemy: Enemy) => void;
    takeDamage: (damage: number) => void;
    gainExp: (exp: number) => void;
    gainLevel: () => void;
    gainGold: (amount: number) => void;
    spendGold: (amount: number) => void;
};

type Enemy = {
    name: string;
    hp: number;
    attack: number;
    exp: number;
    gold: number;
}

const useAppStore = create<Store>(set => ({
    level: 1,
    hp: 100,
    maxHp: 100,
    attack: 10,
    exp: 0,
    gold: 0,
    enemy: null,
    setEnemy: (enemy: Enemy) => set({ enemy }),
    takeDamage: damage => set(state => ({hp: state.hp - damage})),
    gainExp: (exp: number) => set(state => ({exp: state.exp + exp})),
    gainLevel: () => set(state => ({level: state.level + 1})),
    gainGold: (amount: number) => set(state => ({gold: state.gold + amount})),
    spendGold: (amount: number) => set(state => ({gold: state.gold + amount})),
}));

export default useAppStore;
