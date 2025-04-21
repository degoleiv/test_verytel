import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Form } from './modules/register/component/Form'
import { ToastContainer } from 'react-toastify';
import { Validation } from './modules/verification/component/Validation';
import { ProtectedRoute } from './modules/verification/component/ProtectedRoute';
import { ValidationProvider } from './modules/verification/hooks/ValidationContext';
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ValidationProvider>
    <ToastContainer />
    <Router>
      <Routes>
        <Route path="/" element={<Form></Form>} />           
        <Route path="/validation" element={
            <ProtectedRoute>
              <Validation />
            </ProtectedRoute>
          } />
        <Route path="*" element={<>No se encontro el recurso</>  }   />  
      </Routes>
    </Router>
    </ValidationProvider>
  </StrictMode>,
)
