import { useState } from 'react';

export function useFormValidation(onSubmit) {
    const [values, setValues] = useState({});
    const [errors, setErrors] = useState({});
    const [isSubmitting, setIsSubmitting] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setValues((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    const validate = () => {
        const newErrors = {};

        // Validaciones personalizadas
        if (!values.nombres) newErrors.nombres = 'El primer nombre es obligatorio';
        if (!values.apellidos) newErrors.apellidos = 'El primer apellido es obligatorio';
        if (!values.tipo_documento) newErrors.tipo_documento = 'El tipo de documento es obligatorio';
        if (!values.identificacion) newErrors.identificacion = 'El número de identificación es obligatorio';

        if (!values.correo) {
            newErrors.correo = 'El correo es obligatorio';
        } else if (!/\S+@\S+\.\S+/.test(values.correo)) {
            newErrors.correo = 'Correo electrónico no válido';
        }

        if (!values.celular) {
            newErrors.celular = 'El celular es obligatorio';
        } else if (!/^\d{10}$/.test(values.celular)) {
            newErrors.celular = 'Número de celular inválido';
        }

        if (!values.barrio) newErrors.barrio = 'El barrio es obligatorio';
        if (!values.direccion) newErrors.direccion = 'La dirección es obligatoria';
        if (!values.fecha_nacimiento) newErrors.fecha_nacimiento = 'La fecha de nacimiento es obligatoria';
        if (!values.sexo) newErrors.sexo = 'El sexo es obligatorio';
        if (!values.frente_seguridad_id) newErrors.frente_seguridad_id = 'Debe seleccionar un frente de seguridad';
        if (!values.antecedentes) newErrors.antecedentes = 'La respuesta a antecedentes es obligatoria';

        if (values.antecedentes === "true" && !values.justificacion_antecedentes) {
            newErrors.justificacion_antecedentes = 'La justificación es obligatoria cuando tiene antecedentes';
        }

        setErrors(newErrors);
        return newErrors;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const validationErrors = validate();
        if (Object.keys(validationErrors).length === 0) {
            setIsSubmitting(true);
            try {
                await onSubmit(values); // 💡 lógica externa definida por el componente
                
            } catch (error) {
                console.error('Error al enviar datos:', error);
            } finally {
                setIsSubmitting(false);
            }
        }
    };

    return {
        values,
        errors,
        handleChange,
        handleSubmit,
        isSubmitting,
    };
}
