import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';

export function useRefreshCode() {
    const [isLoading, setIsLoading] = useState(false);
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const url = 'http://127.0.0.1:8000/signin/refresh'; // Corregido: eliminamos el doble //.

    const submit = async () => {
        setIsLoading(true); // Inicia la carga
        setError(null); // Reinicia el error
        setResponse(null); // Reinicia la respuesta
        const id = sessionStorage.getItem("userId");

        try {
            const res = await fetch(`${url}?id=${id}`, { // Corregido: Usamos un solo & para los parámetros
                method: 'GET',
                headers: { 'Content-Type': 'application/json' },
            });

            const result = await res.json();

            if (!res.ok) {
                throw new Error(result.detail || 'Hubo un error en la autenticación'); // Mensaje de error personalizado
            }

            setResponse(result); // Guarda la respuesta exitosa
            toast.info(result.message); // Muestra un mensaje de éxito
           
        } catch (err) {
            setError(err.message); // Guarda el error
            toast.error(err.message); // Muestra un mensaje de error
        } finally {
            setIsLoading(false); // Finaliza el estado de carga
        }
    };

    return { submit, isLoading, response, error }; // Devolvemos el estado
}
