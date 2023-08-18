import { useState } from "react";

import {baseUrl} from "../constants"

const Predict = () => {
    const [text, setText] = useState("");
    const handleFormSubmit = async(e: any) =>{
        e.preventDefault();
        if (text === "") {
            alert("Please enter a text")
            return
        }

        const res = await fetch(`${baseUrl}/predict`, {
            body: JSON.stringify({
                review: text
            }),
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
        });
        if (res.status === 200) {
            const data = await res.json();
            console.log(data)
            alert("Prediction: " + data.sentiment)
        } else {
            alert("Something went wrong. Please try again.")
        }



    }



    return (
        <div>

<section className="bg-white dark:bg-gray-900">
  <div className="py-8 lg:py-16 px-4 mx-auto max-w-screen-md">
      <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-center text-gray-900 dark:text-white">Predict</h2>
      <br />
        <br />
      <form className="space-y-8">
          <div className="sm:col-span-2">
              <label htmlFor="message" className="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400">Your Text ...</label>
              <textarea id="message" rows={8} className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white 
              dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Start Typing ..."
                onChange={(e) => setText(e.target.value)}
              
              ></textarea>
          </div>
          <button type="submit" className="py-3 px-5 text-sm font-medium text-center text-white rounded-lg bg-blue-700 sm:w-fit hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            onClick={handleFormSubmit}
          
          >
            
            Predict Now

          </button>
      </form>
  </div>
</section>

        </div>


    )
}

export default Predict