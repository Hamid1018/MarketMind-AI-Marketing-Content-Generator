import { useState } from "react";


const API_URL = "http://localhost:8000";


const initialForm = {

  product_name: "",

  product_description: "",

  target_audience: "",

  marketing_platform: "Instagram",

  campaign_objective:
    "Increase product awareness",

  tone: "Professional",

  preferred_language: "English"
};


function App() {

  const [form, setForm] =
    useState(initialForm);

  const [strategy, setStrategy] =
    useState(null);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const [message, setMessage] =
    useState("");

  const [campaignId, setCampaignId] =
    useState(null);


  const updateField = (event) => {

    setForm((current) => ({

      ...current,

      [event.target.name]:
        event.target.value

    }));

  };


  const validate = () => {

    if (
      form.product_name.trim().length < 2
    ) {
      return "Product name must be at least 2 characters.";
    }


    if (
      form.product_description
        .trim()
        .length < 20
    ) {
      return "Product description must be at least 20 characters.";
    }


    if (
      form.target_audience.trim().length < 3
    ) {
      return "Please describe the target audience.";
    }


    if (
      form.campaign_objective
        .trim()
        .length < 5
    ) {
      return "Campaign objective is required.";
    }


    if (
      form.preferred_language
        .trim()
        .length < 2
    ) {
      return "Preferred language is required.";
    }


    return "";
  };


  const submit = async (event) => {

    event.preventDefault();

    setError("");
    setMessage("");
    setStrategy(null);
    setCampaignId(null);


    const validationError =
      validate();


    if (validationError) {

      setError(validationError);

      return;
    }


    setLoading(true);


    try {

      const response = await fetch(

        `${API_URL}/api/campaigns/strategy`,

        {

          method: "POST",

          headers: {
            "Content-Type":
              "application/json"
          },

          body: JSON.stringify(form)

        }
      );


      const data =
        await response.json();


      if (!response.ok) {

        throw new Error(
          data.detail ||
          "Request failed."
        );

      }


      setStrategy(data.strategy);

      setCampaignId(data.id);

      setMessage(data.message);

    }

    catch (requestError) {

      setError(
        requestError.message ||
        "Could not connect to the backend."
      );

    }

    finally {

      setLoading(false);

    }

  };


  return (

    <div className="page-shell">

      <header className="hero">

        <div>

          <p className="eyebrow">
            DAY 22 · PHASE 1
          </p>

          <h1>
            AI Marketing Strategy Generator
          </h1>

          <p className="hero-copy">

            Enter your product and campaign
            information and generate a
            structured AI marketing strategy.

          </p>

        </div>


        <div className="stack-badge">

          React + FastAPI + OpenAI

        </div>

      </header>


      <main className="main-grid">


        {/* FORM */}

        <section className="card form-card">

          <div className="card-heading">

            <div>

              <h2>
                Campaign Brief
              </h2>

              <p>
                Complete all required fields.
              </p>

            </div>

            <span>
              * Required
            </span>

          </div>


          <form onSubmit={submit}>


            <label>

              Product Name *

              <input

                name="product_name"

                value={form.product_name}

                onChange={updateField}

                placeholder="e.g. SmartFit Bottle"

              />

            </label>


            <label>

              Product Description *

              <textarea

                name="product_description"

                value={
                  form.product_description
                }

                onChange={updateField}

                rows="5"

                placeholder="Describe the product and what makes it useful."

              />

            </label>


            <label>

              Target Audience *

              <input

                name="target_audience"

                value={form.target_audience}

                onChange={updateField}

                placeholder="e.g. university students"

              />

            </label>


            <div className="two-col">


              <label>

                Marketing Platform *

                <select

                  name="marketing_platform"

                  value={
                    form.marketing_platform
                  }

                  onChange={updateField}

                >

                  <option>
                    Instagram
                  </option>

                  <option>
                    LinkedIn
                  </option>

                  <option>
                    Facebook
                  </option>

                  <option>
                    YouTube
                  </option>

                </select>

              </label>


              <label>

                Tone *

                <select

                  name="tone"

                  value={form.tone}

                  onChange={updateField}

                >

                  <option>
                    Professional
                  </option>

                  <option>
                    Friendly
                  </option>

                  <option>
                    Bold
                  </option>

                  <option>
                    Luxury
                  </option>

                  <option>
                    Playful
                  </option>

                  <option>
                    Educational
                  </option>

                </select>

              </label>


            </div>


            <label>

              Campaign Objective *

              <input

                name="campaign_objective"

                value={
                  form.campaign_objective
                }

                onChange={updateField}

                placeholder="e.g. generate leads"

              />

            </label>


            <label>

              Preferred Language *

              <input

                name="preferred_language"

                value={
                  form.preferred_language
                }

                onChange={updateField}

                placeholder="e.g. English"

              />

            </label>


            {error && (

              <div className="alert error">

                {error}

              </div>

            )}


            {message && (

              <div className="alert success">

                {message}

                <br />

                Campaign ID:
                #{campaignId}

              </div>

            )}


            <button
              type="submit"
              disabled={loading}
            >

              {loading

                ? "Generating Strategy..."

                : "Generate Marketing Strategy"

              }

            </button>


          </form>

        </section>


        {/* RESULT */}

        <section className="card result-card">

          <div className="card-heading">

            <div>

              <h2>
                AI Strategy
              </h2>

              <p>
                Structured output for
                later phases.
              </p>

            </div>

            <span>
              Strategy Only
            </span>

          </div>


          {!strategy ? (

            <div className="empty-state">

              <h3>
                No strategy yet
              </h3>

              <p>

                Submit the campaign brief
                to generate the AI marketing
                strategy.

              </p>

            </div>

          ) : (

            <div className="strategy">

              <StrategyItem
                title="Campaign Idea"
                value={
                  strategy.campaign_idea
                }
              />


              <StrategyItem
                title="Campaign Objective"
                value={
                  strategy.campaign_objective
                }
              />


              <StrategyItem
                title="Target Audience"
                value={
                  strategy.target_audience
                }
              />


              <StrategyItem
                title="Audience Angle"
                value={
                  strategy.audience_angle
                }
              />


              <StrategyList

                title="Key Selling Points"

                items={
                  strategy.key_selling_points
                }

              />


              <StrategyItem

                title="Key Message"

                value={
                  strategy.key_message
                }

              />


              <StrategyList

                title="Content Pillars"

                items={
                  strategy.content_pillars
                }

              />


              <StrategyItem

                title="Content Tone"

                value={
                  strategy.content_tone
                }

              />


              <StrategyItem

                title="Call to Action"

                value={
                  strategy.call_to_action
                }

              />


              <StrategyList

                title="Suggested Content Types"

                items={
                  strategy.suggested_content_types
                }

              />


              <StrategyItem

                title="Why This Platform"

                value={
                  strategy.platform_reason
                }

              />

            </div>

          )}

        </section>


      </main>

    </div>

  );
}


function StrategyItem({
  title,
  value
}) {

  return (

    <div className="strategy-block">

      <h3>
        {title}
      </h3>

      <p>
        {value}
      </p>

    </div>

  );
}


function StrategyList({
  title,
  items
}) {

  return (

    <div className="strategy-block">

      <h3>
        {title}
      </h3>

      <ul>

        {items.map(
          (item, index) => (

            <li
              key={`${item}-${index}`}
            >
              {item}
            </li>

          )
        )}

      </ul>

    </div>

  );
}


export default App;