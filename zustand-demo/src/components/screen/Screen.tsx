import background from '../../assets/background.png';
import useAppStore from '../../store';
import styles from './Screen.module.css';

function Screen() {
    const enemy = useAppStore((state) => state.enemy);

    return (
        <div>
            <img src={background} alt="Background" className={styles.screen} />
        </div>
    );
}

export default Screen;