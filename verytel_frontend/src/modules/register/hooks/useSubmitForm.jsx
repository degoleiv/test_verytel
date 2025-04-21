import { useState } from 'react';
import {  toast } from 'react-toastify';
import { useValidation } from '../../verification/hooks/ValidationContext';
import { useNavigate } from 'react-router-dom';
export function useSubmitForm() {
    const [isLoading, setIsLoading] = useState(false);
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);
    const { setIsPendingValidation } = useValidation();
    const navigate = useNavigate();
    const url = 'http://127.0.0.1:8000/signin/register';
    const submit = async (data) => {
        setIsLoading(true);
        setError(null);
        try {
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
           
            const result = await res.json();
            
            if (!res.ok){
                throw new Error(result.detail);
            }
            toast.info(result.message);
            setIsPendingValidation(true);
            sessionStorage.setItem("userId", data.identificacion);
            navigate("/validation");
            setResponse(result);
            
            return result; // para que el componente lo use si lo necesita
        } catch (err) {
            
            toast.error(''+ err);
            setError(err || 'Error desconocido');
        } finally {
            setIsLoading(false);
        }
    };

    return { submit, isLoading, response, error };
}
