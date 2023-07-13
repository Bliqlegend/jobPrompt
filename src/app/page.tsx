'use client'
import { useState } from 'react'
import axios from 'axios'
import Loader from './Loader'
import { Button, Modal } from 'antd'
import { toast } from 'react-hot-toast'
import { Toaster } from 'react-hot-toast'

export default function Contact() {
  const [selectedOption, setSelectedOption] = useState('')
  const [companyJD, setCompanyJD] = useState('')
  const [contactPoint, setContactPoint] = useState('')
  const [heading, setHeading] = useState('Company JD')
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState('')
  const [modalIsOpen, setModalIsOpen] = useState(false)
  const handleApplicationGenerate = async () => {
    setLoading(true)
    try {
      const response = await axios.post(
        'https://jobprompt.wereon.in/generate_application_message/',
        {
          contactPoint: contactPoint,
          companyJD: companyJD,
        }
      )
      console.log(response.data[0].message)
      setMessage(response.data[0].message)
      handleShowModal()
    } catch (error) {
      console.error(error)
    }
    setLoading(false)
  }

  const handleDMGenerate = async () => {
    setLoading(true)
    try {
      const response = await axios.post(
        'https://jobprompt.wereon.in/generate_dm_message/',
        {
          contactPoint: contactPoint,
          companyJD: companyJD,
        }
      )
      console.log(response.data[0].message)
      setMessage(response.data[0].message)
      handleShowModal()
    } catch (error) {
      console.error(error)
    }
    setLoading(false)
  }
  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedOption(e.target.value)
    if (e.target.value === 'DM') {
      setHeading('Message Posted')
    } else {
      setHeading('Company JD')
    }
  }

  const handleGenerateCall = () => {
    if (selectedOption === 'DM') {
      handleDMGenerate()
    } else {
      handleApplicationGenerate()
    }
  }

  const handleShowModal = () => {
    setModalIsOpen(true)
  }

  const handleCloseModal = () => {
    setModalIsOpen(false)
    setMessage('')
    setContactPoint('')
  }

  const handleCopy = async () => {
    await navigator.clipboard
      .writeText(message)
      .then(() => toast.success('Successfully copied to clipboard'))
      .catch(() => toast.error('Failed to copy text'))
  }

  const handleOk = () => {
    setLoading(true)
    setTimeout(() => {
      setLoading(false)
      setModalIsOpen(false)
    }, 3000)
  }

  return (
    <>
      {loading && <Loader />}
      <Toaster />

      <Modal
        open={modalIsOpen}
        title="Generated Message"
        onCancel={handleCloseModal}
        footer={[
          <Button key="back" onClick={handleCloseModal}>
            Close
          </Button>,
          <Button
            key="link"
            type="dashed"
            loading={loading}
            onClick={handleCopy}
          >
            Copy to ClipBoard
          </Button>,
        ]}
      >
        <p>{message}</p>
      </Modal>

      <div className="flex flex-col h-screen justify-center items-center bg-gray-200">
        <div className="w-full max-w-md">
          <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
            <div className="mb-4">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="dropdown"
              >
                Select Type
              </label>
              <div className="inline-block relative w-64">
                <select
                  value={selectedOption}
                  onChange={handleChange}
                  className="block appearance-none w-full bg-white border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                  id="grid-state"
                >
                  <option value="Application">Application</option>
                  <option value="DM">DM</option>
                </select>
                <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                  <svg
                    className="fill-current h-4 w-4"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                  </svg>
                </div>
              </div>
            </div>
            <div className="mb-6">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="point-of-contact"
              >
                Point of Contact
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-12"
                id="point-of-contact"
                type="text"
                placeholder="Contact Point"
                value={contactPoint}
                onChange={(e) => setContactPoint(e.target.value)}
              />
            </div>
            <div className="mb-6">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="company-jd"
              >
                {heading}
              </label>
              <textarea
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                id="company-jd"
                placeholder="Enter details here..."
                value={companyJD}
                onChange={(e) => setCompanyJD(e.target.value)}
              ></textarea>
            </div>
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="button"
              onClick={handleGenerateCall}
            >
              Generate
            </button>
          </div>
        </div>
      </div>
    </>
  )
}
