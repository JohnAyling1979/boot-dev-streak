import useAppStore from '../../store';
import { enemies } from '../../constants';

function Controls() {
    const enemy = useAppStore(state => state.enemy);
    const playerAttack = useAppStore(state => state.attack);
    const playerHp = useAppStore(state => state.hp);

    const takeDamage = useAppStore(state => state.takeDamage);
    const gainExp = useAppStore(state => state.gainExp);
    const gainGold = useAppStore(state => state.gainGold);
    const setEnemy = useAppStore(state => state.setEnemy);

    const search = () => {
        const randomIndex = Math.floor(Math.random() * enemies.length);
        const newEnemy = JSON.parse(JSON.stringify(enemies[randomIndex]));

        setEnemy(newEnemy);
    }

    const attack = () => {
        if (enemy) {
            enemy.hp -= playerAttack;

            if (enemy.hp <= 0) {
                setEnemy(null);
                gainGold(enemy.gold);
                gainExp(enemy.exp);
            } else {
                takeDamage(enemy.attack);
            }
        }
    }

    return (
        <div>
            {enemy && (
                <div>
                    <h2>Enemy: {enemy.name}</h2>
                    <p>HP: {enemy.hp}</p>
                    <button onClick={attack}>Attack</button>
                </div>
            )}
            {!enemy && <button onClick={search}>Search</button>}
        </div>
    );
}

export default Controls;