import { useState, useEffect } from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { onAuthStateChanged } from 'firebase/auth'
import { auth } from './firebaseConfig'
import LoginPage from './pages/LoginPage'
import CompanyPage from './pages/CompanyPage'
import MaterialListingPage from './pages/MaterialListingPage'

function App() {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user)
      setLoading(false)
    })

    return () => unsubscribe()
  }, [])

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center">Cargando...</div>
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Routes>
        <Route path="/login" element={!user ? <LoginPage /> : <Navigate to="/company" />} />
        <Route path="/company" element={user ? <CompanyPage /> : <Navigate to="/login" />} />
        <Route path="/materials" element={user ? <MaterialListingPage /> : <Navigate to="/login" />} />
        <Route path="/" element={<Navigate to={user ? "/company" : "/login"} />} />
      </Routes>
    </div>
  )
}

export default App