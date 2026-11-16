import React from 'react'
import "./Button.css"

export default function Button({name, type, onClick}) {
  return (
    <button type={type} className="btn w-100 btn-styled" onClick={onClick}>{name}</button>
  )
}
