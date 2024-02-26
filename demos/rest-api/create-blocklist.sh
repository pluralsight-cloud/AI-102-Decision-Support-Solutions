curl --location --request PATCH "${CONTENT_SAFETY_ENDPOINT}contentsafety/text/blocklists/code-words?api-version=2023-10-01" \
--header "Ocp-Apim-Subscription-Key: ${CONTENT_SAFETY_KEY}" \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "This is a code-words list"
}'