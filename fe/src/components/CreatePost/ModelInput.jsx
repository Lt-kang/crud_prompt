const modelOptions = [
    'gpt-4.1',
    'gpt-5',
    'gpt-5-nano',
    'gpt-5-mini',
    ]
export default function ModelInput({ postObj, handleInputChange }) {
    return (
      <div className="form-group">
        <label htmlFor="model">Model</label>
          <select
            id="model"
            name="model"
            value={postObj.model || "gpt-4.1"}
            onChange={handleInputChange}
            required
          >
            <option value="">모델을 선택하세요</option>
            {modelOptions.map(option => (
              <option key={option} 
                      value={option}>
                        {option}
              </option>
            ))}
          </select>
      </div>
    )
  }
  