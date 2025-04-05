import useAppStore from "../../store";
import styles from "./Stats.module.css";

function Stats() {
    const hp = useAppStore((state) => state.hp);
    const maxHp = useAppStore((state) => state.maxHp);
    const level = useAppStore((state) => state.level);
    const attack = useAppStore((state) => state.attack);
    const exp = useAppStore((state) => state.exp);
    const gold = useAppStore((state) => state.gold);

    return (
        <div>
            <div className={styles.statSection}>
                <h2>Level:</h2>
                <p>{level}</p>
            </div>
            <div className={styles.statSection}>
                <h2>HP:</h2>
                <p>{hp}/{maxHp}</p>
            </div>
            <div className={styles.statSection}>
                <h2>Attack:</h2>
                <p>{attack}</p>
            </div>
            <div className={styles.statSection}>
                <h2>EXP:</h2>
                <p>{exp}</p>
            </div>
            <div className={styles.statSection}>
                <h2>Gold:</h2>
                <p>{gold}</p>
            </div>
        </div>
    );
}

export default Stats;
