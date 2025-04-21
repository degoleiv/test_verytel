import React, { useState } from 'react';
import { useFormValidation } from '../hooks/registerFormValidation';
import useSecurityFrontsList from '../hooks/useSecurityFrontList';
import '../assets/Form.css'
import { useSubmitForm } from '../hooks/useSubmitForm';

export function Form() {
  const { submit, isLoading, response, error } = useSubmitForm();
 
  const {
    values,
    errors,
    handleChange,
    handleSubmit,
    isSubmitting,
  } = useFormValidation(submit); // Le pasas la función del hook

  const { data, list_error } = useSecurityFrontsList();

  return (
    <div className='container_form'>
    <h1>Registro de Abonados a Frentes de Seguridad </h1>
   
    <form className='form-inline' onSubmit={handleSubmit}>
      <div>
        <label htmlFor="nombres">Primer Nombre</label>
        <input
          type="text"
          id="nombres"
          name="nombres"
          value={values.nombres || ''}
          onChange={handleChange}
          className={errors.nombres ? "input-error" : ""}
        />
        {errors.nombres && <span>{errors.nombres}</span>}
      </div>

      <div>
        <label htmlFor="apellidos">Primer Apellido</label>
        <input
          type="text"
          id="apellidos"
          name="apellidos"
          value={values.apellidos || ''}
          onChange={handleChange}
          className={errors.apellidos ? "input-error" : ""}
        />
        {errors.apellidos && <span>{errors.apellidos}</span>}
      </div>

      <div>
        <label htmlFor="tipo_documento">Tipo de documento</label>
        <select
          id="tipo_documento"
          name="tipo_documento"
          value={values.tipo_documento || ''}
          onChange={handleChange}
          className={errors.tipo_documento ? "input-error" : ""}
        >
          <option value="">Seleccione...</option>
          <option value="CC">Cédula de ciudadanía</option>
          <option value="CE">Cédula de extranjería</option>
          <option value="TI">Tarjeta de identidad</option>
          <option value="Pasaporte">Pasaporte</option>
        </select>
        {errors.tipo_documento && <span>{errors.tipo_documento}</span>}
      </div>

      <div>
        <label htmlFor="identificacion">Número de identificación</label>
        <input
          type="text"
          id="identificacion"
          name="identificacion"
          value={values.identificacion || ''}
          onChange={handleChange}
          className={errors.identificacion ? "input-error" : ""}
        />
        {errors.identificacion && <span>{errors.identificacion}</span>}
      </div>

      <div>
        <label htmlFor="correo">Correo electrónico</label>
        <input
          type="email"
          id="correo"
          name="correo"
          value={values.correo || ''}
          onChange={handleChange}
          className={errors.correo ? "input-error" : ""}
        />
        {errors.correo && <span>{errors.correo}</span>}
      </div>

      <div>
        <label htmlFor="celular">Número de celular</label>
        <input
          type="tel"
          id="celular"
          name="celular"
          value={values.celular || ''}
          onChange={handleChange}
          className={errors.celular ? "input-error" : ""}
        />
        {errors.celular && <span>{errors.celular}</span>}
      </div>

      <div>
        <label htmlFor="barrio">Barrio</label>
        <input
          type="text"
          id="barrio"
          name="barrio"
          value={values.barrio || ''}
          onChange={handleChange}
          className={errors.barrio ? "input-error" : ""}
        />
        {errors.barrio && <span>{errors.barrio}</span>}
      </div>

      <div>
        <label htmlFor="direccion">Dirección exacta</label>
        <input
          type="text"
          id="direccion"
          name="direccion"
          value={values.direccion || ''}
          onChange={handleChange}
          className={errors.direccion ? "input-error" : ""}
        />
        {errors.direccion && <span>{errors.direccion}</span>}
      </div>

      <div>
        <label htmlFor="fecha_nacimiento">Fecha de nacimiento</label>
        <input
          type="date"
          id="fecha_nacimiento"
          name="fecha_nacimiento"
          value={values.fecha_nacimiento || ''}
          onChange={handleChange}
          className={errors.fecha_nacimiento ? "input-error" : ""}
        />
        {errors.fecha_nacimiento && <span>{errors.fecha_nacimiento}</span>}
      </div>

      {data && (
        <div>
          <label htmlFor="frente_seguridad_id">Frente de Seguridad asociado</label>
          <select
            id="frente_seguridad_id"
            name="frente_seguridad_id"
            value={values.frente_seguridad_id || ''}
            onChange={handleChange}
            className={errors.frente_seguridad_id ? "input-error" : ""}
          >
            <option value="">Seleccione...</option>
            {data.map((item, index) => (
              <option key={index} value={item.id}>
                {item.nombre}
              </option>
            ))}
          </select>
          {errors.frente_seguridad_id && <span>{errors.frente_seguridad_id}</span>}
        </div>
      )}

      <div>
        <label htmlFor="sexo">Sexo</label>
        <select
          id="sexo"
          name="sexo"
          value={values.sexo || ''}
          onChange={handleChange}
          className={errors.sexo ? "input-error" : ""}
        >
          <option value="">Seleccione...</option>
          <option value="M">Masculino</option>
          <option value="F">Femenino</option>
          <option value="NB">No binario</option>
          <option value="ND">Prefiero no decirlo</option>
        </select>
        {errors.sexo && <span>{errors.sexo}</span>}
      </div>

      <div>
        <label htmlFor="antecedentes">¿Tiene antecedentes?</label>
        <select
          id="antecedentes"
          name="antecedentes"
          value={values.antecedentes || ''}
          onChange={handleChange}
          className={errors.antecedentes ? "input-error" : ""}
        >
          <option value="">Seleccione...</option>
          <option value="false">No</option>
          <option value="true">Sí</option>
        </select>
        {errors.antecedentes && <span>{errors.antecedentes}</span>}
      </div>

      {values.antecedentes === "true" && (
        <div>
          <label htmlFor="justificacion_antecedentes">Justificación</label>
          <textarea
            id="justificacion_antecedentes"
            name="justificacion_antecedentes"
            value={values.justificacion_antecedentes || ''}
            onChange={handleChange}
            className={errors.justificacion_antecedentes ? "input-error" : ""}
          ></textarea>
          {errors.justificacion_antecedentes && <span>{errors.justificacion_antecedentes}</span>}
        </div>
      )}

      <button type="submit" disabled={isSubmitting}>Enviar</button>

     
    </form>
    </div>
  );
}
