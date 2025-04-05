import Controls from './components/controls/Controls'
import Screen from './components/screen/Screen'
import Stats from './components/stats/Stats'
import styles from './App.module.css'

function App() {
  return (
    <>
      <Screen />
      <div className={styles.lowerSection}>
        <Stats />
        <Controls />
      </div>
    </>
  )
}

export default App
