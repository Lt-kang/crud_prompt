import { useState } from "react";




const modelOptions = {
    openai: [
    'gpt-4.1',
    'gpt-4o',
    'gpt-5',
    'gpt-5-nano',
    'gpt-5-mini',
    ],

    // anthropic: [
    // 'claude-3-5-sonnet-20240620',
    // 'claude-3-5-sonnet-20240621',
    // ],

    google: [
    'gemini-2.0-flash',
    'gemini-2.5-pro',
    ]
}



export default function ModelInput({ postObj, handleInputChange }) {
  const companyList = Object.keys(modelOptions);
  const [company, setCompany] = useState(companyList[0]);
  const [modelList, setModelList] = useState(modelOptions[company]);
  const [model, setModel] = useState(modelList[0]);

  const handleCompanyChange = (e) => {
    const value = e.target.value;

    setCompany(value);
    setModelList(modelOptions[value]);
    setModel(modelList[0]);
    handleInputChange(e);
  };

  const handleModelChange = (e) => {
    setModel(e.target.value);
    handleInputChange(e);
  };


    return (
      <>
        <div className="form-group">
          <label htmlFor="company">Company</label>
          <select
              id="company"
              name="company"
              value={company}
              onChange={handleCompanyChange}
              required
          >
              {companyList.map(option => (
                  <option key={option} value={option}>{option}</option>
              ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="model">Model</label>
            <select
              id="model"
              name="model"
              value={model}
              onChange={handleModelChange}
              required
            >
              {modelList.map(option => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
        </div>
      </>
    )
  }
  