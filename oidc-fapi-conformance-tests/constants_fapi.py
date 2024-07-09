
ALIAS = "fapi-wso2is"

BASE_URL = "https://iam:9443"
DCR_ENDPOINT = BASE_URL + "/api/identity/oauth2/dcr/v1.1/register"
TOKEN_ENDPOINT = BASE_URL + "/oauth2/token"
APPLICATION_ENDPOINT = BASE_URL + "/api/server/v1/applications"
CREATE_USER_ENDPOINT = BASE_URL + "/scim2/Users"
RESOURCE_ENDPOINT_URL = "https://iam/resource"

SCOPES = "internal_user_mgt_update internal_application_mgt_create internal_application_mgt_view internal_login " \
         "internal_claim_meta_update internal_application_mgt_update internal_scope_mgt_create"

SET_SCOPE_CLAIMS_BODY_PAYLOAD = {
    "claimConfiguration": {
        "dialect": "LOCAL",
        "requestedClaims": [
            {
                "claim": {
                    "uri": "http://wso2.org/claims/username"
                },
                "mandatory": "false"
            }
        ]
    }
}

DISABLE_SKIP_CONSENT_BODY_PAYLOAD = {
    "advancedConfigurations": {
        "skipLoginConsent": "false"
    }
}

HEADERS_WITH_AUTH = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
               'Authorization': 'Basic YWRtaW46YWRtaW4='}

# SP App common configs

DCR_BODY = {
    "grant_types": ["client_credentials", "authorization_code", "refresh_token"],
    "backchannel_logout_uri": "https://www.google.com",
    "backchannel_logout_session_required": "true",
    "token_endpoint_auth_signing_alg" : "PS256",
    "id_token_signed_response_alg" : "PS256",
    "id_token_encrypted_response_alg" : "RSA-OAEP",
    "id_token_encrypted_response_enc" : "A128GCM",
    "request_object_signing_alg" : "PS256",
    "require_signed_request_object" : "true",
    "tls_client_certificate_bound_access_tokens":"true",
    "request_object_encryption_alg" : "RSA-OAEP",
    "request_object_encryption_enc" : "A128GCM",
}

ACR = {
        "authenticationSequence": {
            "attributeStepId": 1,
            "steps": [
                {
                    "id": 1,
                    "options": [
                        {
                            "authenticator": "BasicAuthenticator",
                            "idp": "LOCAL"
                        }
                    ]
                }
            ],
            "subjectStepId": 1,
            "type": "USER_DEFINED",
            "script": "var supportedAcrValues = ['acr1', 'urn:mace:incommon:iap:silver',];\n\nvar onLoginRequest = function(context) {\n    var selectedAcr = selectAcrFrom(context, supportedAcrValues);\n    Log.info('--------------- ACR selected: ' + selectedAcr);\n    context.selectedAcr = selectedAcr;\n    executeStep(1);\n};\n"
        }
}

# SP App configs

JWKS_1 = "http://localhost:5002/jwks1"
JWKS_2 = "http://localhost:5002/jwks2"


PVTKEYJWT_APP1 = {
    "client_name": "pvtkeyjwt_fapi1",
    "token_endpoint_auth_method": "private_key_jwt",
    "client_id": "pvtkeyjwt_fapi1_client_id",
    "client_secret": "pvtkeyjwt_fapi1_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback"],
    "jwks_uri": JWKS_1,
    "require_pushed_authorization_requests" : "false",
}

PVTKEYJWT_APP2 = {
    "client_name": "pvtkeyjwt_fapi2",
    "token_endpoint_auth_method": "private_key_jwt",
    "client_id": "pvtkeyjwt_fapi2_client_id",
    "client_secret": "pvtkeyjwt_fapi2_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback?dummy1=lorem&dummy2=ipsum"],
    "jwks_uri": JWKS_2,
    "require_pushed_authorization_requests" : "false",
}

MTLS_APP1 = {
    "client_name": "mtls_fapi1",
    "token_endpoint_auth_method": "tls_client_auth",
    "client_id": "mtls_fapi1_client_id",
    "client_secret": "mtls_fapi1_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback"],
    "jwks_uri": JWKS_1,
    "require_pushed_authorization_requests" : "false",
}

MTLS_APP2 = {
    "client_name": "mtls_fapi2",
    "token_endpoint_auth_method": "tls_client_auth",
    "client_id": "mtls_fapi2_client_id",
    "client_secret": "mtls_fapi2_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback?dummy1=lorem&dummy2=ipsum"],
    "jwks_uri": JWKS_2,
    "require_pushed_authorization_requests" : "false",
}

PVTKEYJWT_PAR_APP1 = {
    "client_name": "pvtkeyjwt_par_fapi1",
    "token_endpoint_auth_method": "private_key_jwt",
    "client_id": "pvtkeyjwt_par_fapi1_client_id",
    "client_secret": "pvtkeyjwt_par_fapi1_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback"],
    "jwks_uri": JWKS_1,
    "require_pushed_authorization_requests" : "true",
}

PVTKEYJWT_PAR_APP2 = {
    "client_name": "pvtkeyjwt_par_fapi2",
    "token_endpoint_auth_method": "private_key_jwt",
    "client_id": "pvtkeyjwt_par_fapi2_client_id",
    "client_secret": "pvtkeyjwt_par_fapi2_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback?dummy1=lorem&dummy2=ipsum"],
    "jwks_uri": JWKS_2,
    "require_pushed_authorization_requests" : "true",
}

MTLS_PAR_APP1 = {
    "client_name": "mtls_par_fapi1",
    "token_endpoint_auth_method": "tls_client_auth",
    "client_id": "mtls_par_fapi1_client_id",
    "client_secret": "mtls_par_fapi1_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback"],
    "jwks_uri": JWKS_1,
    "require_pushed_authorization_requests" : "true",
}

MTLS_PAR_APP2 = {
    "client_name": "mtls_par_fapi2",
    "token_endpoint_auth_method": "tls_client_auth",
    "client_id": "mtls_par_fapi2_client_id",
    "client_secret": "mtls_par_fapi2_client_secret",
    "redirect_uris": ["https://localhost.emobix.co.uk:8443/test/a/fapi-wso2is/callback?dummy1=lorem&dummy2=ipsum"],
    "jwks_uri": JWKS_2,
    "require_pushed_authorization_requests" : "true",
}

ENABLE_HYBRID_FLOW = {
    "enable": "true",
    "responseType": "code id_token"
}

SMTP_SERVER = "smtp.gmail.com"

SMTP_SERVER_PORT = 465
