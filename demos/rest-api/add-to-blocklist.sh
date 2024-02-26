curl --location --request POST "${CONTENT_SAFETY_ENDPOINT}/contentsafety/text/blocklists/code-words:addOrUpdateBlocklistItems?api-version=2023-10-01" \
--header "Ocp-Apim-Subscription-Key: ${CONTENT_SAFETY_KEY}" \
--header 'Content-Type: application/json' \
--data-raw '{
  "blocklistItems": [
    {
      "description": "string",
      "text": "jeepers"
    },
    {
      "description": "string",
      "text": "creepers"
    }
  ]
}'