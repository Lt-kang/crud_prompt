function TextInput({ postObj, handleInputChange, title, id, name, placeholder, required=true }) {
    return (
            <div className="form-group">
                <label htmlFor="title">{title}</label>
                <input
                    type="text"
                    id={id}
                    name={name}
                    value={postObj[name]}
                    onChange={handleInputChange}
                    placeholder={placeholder}
                    required={required}
                />
            </div>
    )
}


function TextareaInput({ postObj, handleInputChange, title, id, name, placeholder, rows=15, required=true }) {
    return (
        <div className="form-group">
        <label htmlFor="prompt-content">{title}</label>
        <textarea
          id={id}
          name={name}
          value={postObj[name]}
          onChange={handleInputChange}
          placeholder={placeholder}
          rows={rows}
          required={required}
        />
      </div>
    )
}



export { TextInput, TextareaInput };



