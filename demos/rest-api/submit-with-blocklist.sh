curl --location --request POST "${CONTENT_SAFETY_ENDPOINT}contentsafety/text:analyze?api-version=2023-10-01" \
--header "Ocp-Apim-Subscription-Key: ${CONTENT_SAFETY_KEY}" \
--header 'Content-Type: application/json' \
--data-raw '{
  "text": "Jeepers, creepers. I hate you and want to beat you up.",
  "categories": [
   "Hate","Sexual","SelfHarm","Violence"
  ],
   "blocklistNames": [
      "code-words"
    ],
   "haltOnBlocklistHit": false
}'