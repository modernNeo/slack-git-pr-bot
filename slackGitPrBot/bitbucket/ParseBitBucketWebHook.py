import hashlib
import hmac
import json


class ParseBitBucketWebHook:

    @staticmethod
    def verify_request(request):
        secret = "Gweujpr3edH1cvEE"
        modified_payload = json.dumps(request.data, separators=(',', ':'), ensure_ascii=False)
        hash_object = hmac.new(
            secret.encode("utf-8"),
            msg=modified_payload.encode("utf-8"),
            digestmod=hashlib.sha256,
        )
        calculated_signature = "sha256=" + hash_object.hexdigest()
        given_signature = request.headers['X-Hub-Signature']
        if not hmac.compare_digest(calculated_signature, given_signature):
            raise Exception(
                "Signatures do not match\nExpected signature:"
                f" {calculated_signature}\nActual: signature: {given_signature}"
            )
        else:
            print("Signatures match")

    @staticmethod
    def parse_comment(payload):
        comment_info = payload['comment']
        comment = comment_info['content']  # noqa: F841
        # Gweujpr3edH1cvEE
